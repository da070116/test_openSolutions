from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models
from . import serializers


class VisitorListView(generics.ListAPIView):
    queryset = models.Visitor.objects.all()
    serializer_class = serializers.VisitorSerializer


class VisitorCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = models.Visitor.objects.all()
    serializer_class = serializers.VisitorSerializer



class LoginView(APIView):
    permission_classes = ()

    # 6c17d7828cfa91ee15fd5f3b4dc25cc4997e076e
# {"username":"test_user", "password":"test_user"}

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        visitor = authenticate(username=username, password=password)

        if visitor:
            return Response({"token": visitor.auth_token.key})
        else:
            return Response({"error": "Wrong credentials"})

