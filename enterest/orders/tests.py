from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.test import APIClient

from enterest.orders.models import Order, Visitor
from enterest.orders.serializers import OrderSerializer, OrderDetailSerializer

client = APIClient()


class TestOrder(TestCase):

    def setUp(self) -> None:
        vis1 = Visitor.objects.create(username="vis1", email="vis1@q.tst", password="123")
        vis2 = Visitor.objects.create(username="vis2", email="vis2@q.tst", password="123")

        Visitor.objects.create_superuser(username="man1", email="man1@re.tst", password="1234")

        Order.objects.create(date="2010-11-11", person=vis1, reason="Reason for enter")
        Order.objects.create(date="2011-11-11", person=vis2, reason="Reason for enter 2")

    def test_get_all_orders(self):
        client.force_authenticate(user=get_user_model())
        response = client.get(reverse('orders_display_all'))
        client.force_authenticate(user=None)
        response_unauthorized = client.get(reverse('orders_display_all'))
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_unauthorized.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_detailed(self):
        client.force_authenticate(user=get_user_model())
        response = client.get("/order-management/display/1")
        response_not_existed = client.get("/order-management/display/404")
        client.force_authenticate(user=None)
        response_unauthorized = client.get('/order-management/display/1')
        order = get_object_or_404(Order, pk=1)
        serializer = OrderDetailSerializer(instance=order, many=False)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response_not_existed.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response_unauthorized.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_order_modify(self):
        client.login(username="man1", password="1234")
        response = client.patch("/order-management/manage/1", {'answer': 'allowed'}, format='json')
        client.logout()
        client.login(username="vis1", password="123")
        response_restricted = client.patch("/order-management/manage/1", {'answer': 'allowed'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_restricted.status_code, status.HTTP_401_UNAUTHORIZED)
