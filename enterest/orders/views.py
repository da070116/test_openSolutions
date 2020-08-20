from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissions

from . import models, serializers


class OrderCreate(generics.CreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class OrderShowList(generics.ListAPIView):
    serializer_class = serializers.OrderSerializer

    def get_queryset(self):
        order_detail = self.kwargs['pk']
        return models.Order.objects.filter(pk=order_detail)


class OrderShowDetailed(generics.RetrieveAPIView):

    serializer_class = serializers.OrderDetailSerializer

    def get_queryset(self):
        order_detail = self.kwargs['pk']
        return models.Order.objects.filter(pk=order_detail)


class OrderManage(generics.RetrieveUpdateAPIView):
    permission_classes = (DjangoModelPermissions,)
    serializer_class = serializers.OrderDetailSerializer

    def get_queryset(self):
        order_to_manage = self.kwargs['pk']
        return models.Order.objects.filter(pk=order_to_manage)
