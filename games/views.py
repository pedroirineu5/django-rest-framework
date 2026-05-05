from rest_framework import generics

from games.models import Games
from rest_framework.permissions import IsAuthenticated
from games.serializers import GamesSerializers


class GamesListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Games.objects.all()
    serializer_class = GamesSerializers

class GamesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Games.objects.all()
    serializer_class = GamesSerializers