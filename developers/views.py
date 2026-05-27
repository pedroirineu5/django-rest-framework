from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from developers.models import Developers
from developers.serializers import DevelopersSerializers
from developers.permissions import  DevelopersPermissionClass

class DevelopersCreateClass(generics.ListCreateAPIView):
    # com base na classe de permissão, agora essas duas views estão trancadas pq elas sempre vao retornar false.
    #
    permission_classes = (IsAuthenticated, DevelopersPermissionClass)
    queryset = Developers.objects.all()
    serializer_class = DevelopersSerializers

class DevelopersDetailUpdateDestroyClass(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, DevelopersPermissionClass)
    queryset = Developers.objects.all()
    serializer_class = DevelopersSerializers