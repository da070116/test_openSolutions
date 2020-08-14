from rest_framework import serializers
from rest_framework.authtoken.models import Token

from . import models


class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Visitor
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        visitor = models.Visitor(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        visitor.set_password(validated_data['password'])
        visitor.save()
        Token.objects.create(user=visitor)
        return visitor


class VisitorViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Visitor
        fields = ('email', 'username',)
