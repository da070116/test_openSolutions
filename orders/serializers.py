from rest_framework import serializers
from . import models


class OrderListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = ('date', 'person', 'reason')


class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = ('date', 'person', 'reason', 'answer')


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = ('date', 'reason')

    def create(self, validated_data):
        order = models.Order(
            date=validated_data['date'],
            reason=validated_data['reason'],
            person=self.context['request'].user
        )

        order.save()
        return order
