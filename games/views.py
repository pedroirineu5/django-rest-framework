from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from games.models import Games
from games.serializers import GamesSerializers


class GamesListCreateView(generics.ListCreateAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializers

class GamesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializers

## isso é usado para coisa fora do crud, coisas customizadas. 
class GamesStatsView(views.APIView):
    permission_classes = (IsAuthenticated)
    queryset = Games.objects.all()


    
    def get()