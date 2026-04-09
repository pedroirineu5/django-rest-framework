from rest_framework import generics

from games.models import Games
from games.serializers import GamesSerializers


class GamesListCreateView(generics.ListCreateAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializers

class GamesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializers