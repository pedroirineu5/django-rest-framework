from django.shortcuts import render
from rest_framework import generics

from platforms.models import Platforms
from platforms.serializers import PlatformSerializers


class PlatformCreateView(generics.ListCreateAPIView):
    queryset = Platforms.objects.all()
    serializer_class = PlatformSerializers

class PlatformRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Platforms.objects.all()
    serializer_class = PlatformSerializers