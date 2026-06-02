from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from platforms.models import Platforms
from platforms.serializers import PlatformSerializers


class PlatformCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Platforms.objects.all()
    serializer_class = PlatformSerializers

class PlatformRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Platforms.objects.all()
    serializer_class = PlatformSerializers