from rest_framework import generics

from games.models import Games


class GamesListCreateView(generics.ListCreateAPIView):
    queryset = Games.objects.all()
    serializer_class = ...

class GamesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Games.objects.all()
    serializer_class = ...