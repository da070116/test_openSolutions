from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissions

from . import models, serializers


class OrderCreate(generics.CreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class OrderList(generics.ListAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class OrderDetail(generics.RetrieveAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderDetailSerializer


class OrderManage(generics.RetrieveUpdateAPIView):
    permission_classes = (DjangoModelPermissions,)
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderDetailSerializer