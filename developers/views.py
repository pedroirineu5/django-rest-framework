from django.shortcuts import render
from rest_framework import generics

from developers.models import Developers
from developers.serializers import DevelopersSerializers


class DevelopersCreateClass(generics.ListCreateAPIView):
    queryset = Developers.objects.all()
    serializer_class = DevelopersSerializers

class DevelopersDetailUpdateDestroyClass(generics.RetrieveUpdateDestroyAPIView):
    queryset = Developers.objects.all()
