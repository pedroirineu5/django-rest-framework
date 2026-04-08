from django.shortcuts import render
from rest_framework import generics

from platforms.models import Platforms
from platforms.serializers import PlatformSerializers


class PlatformCreateView(generics.ListCreateAPIView):
    model = Platforms
    serializer_class = PlatformSerializers

class PlatformRetrieve(generics.RetrieveUpdateDestroyAPIView):
    model = Platforms
    serializer_class = PlatformSerializers