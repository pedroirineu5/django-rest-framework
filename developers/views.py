from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from developers.models import Developers
from developers.serializers import DevelopersSerializers


class DevelopersCreateClass(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Developers.objects.all()
    serializer_class = DevelopersSerializers

class DevelopersDetailUpdateDestroyClass(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Developers.objects.all()
    serializer_class = DevelopersSerializers