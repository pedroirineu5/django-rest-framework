from rest_framework import generics, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK

from reviews.models import Review
from games.models import Games
from games.serializers import GamesSerializers 

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
        total_review = Review.queryset.count()
        return request.Response(
            data={
                "total_game": total_game,
                "total_review": total_review
            },
            status=HTTP_200_OK
        )
