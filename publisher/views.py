from django.shortcuts import render
from rest_framework import generics

from publisher.models import Publisher
from publisher.serializers import PublisherSerializers


class PublisherCreateListView(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializers

class PublisherRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializers