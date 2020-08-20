from rest_framework import generics


from . import models
from . import serializers


class VisitorShowList(generics.ListAPIView):
    queryset = models.Visitor.objects.all()
    serializer_class = serializers.VisitorViewSerializer


class VisitorCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = models.Visitor.objects.all()
    serializer_class = serializers.VisitorSerializer
