from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from publisher.models import Publisher
from publisher.serializers import PublisherSerializers


class PublisherCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializers

class PublisherRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializers