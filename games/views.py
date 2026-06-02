from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django import views
from games.models import Games
from rest_framework.permissions import IsAuthenticated
from games.serializers import GamesSerializers 
from rest_framework.status import HTTP_200_OK

class GamesListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Games.objects.all()
    serializer_class = GamesSerializers

class GamesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Games.objects.all()
    serializer_class = GamesSerializers

## isso é usado para coisa fora do crud, coisas customizadas. 
class GamesStatsView(views.APIView):
    permission_classes = (IsAuthenticated)
    queryset = Games.objects.all()



    def get(self,request):
        total_game = self.queryset.count()

        return request.Response(
            data={
                "total_game": total_game
            },
            status=HTTP_200_OK
        )
