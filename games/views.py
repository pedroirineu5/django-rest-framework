from django.db.models import Avg, Count, Max, Min, Sum
from rest_framework import generics, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK

from games.models import Games
from games.serializers import GamesSerializers, GameStatsSerializers
from reviews.models import Review


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
        total_game = self.queryset.aggregate(total=Count('id'))
        total_review = Review.queryset.Count()
        # total_game_per_genre = Games.objects.Count().aggregate()
        
        game_stats={
                "total_game": total_game,
                "total_review": total_review
            },
        
        serializer = GameStatsSerializers(data=game_stats)
        serializer.is_valid(raise_exception=True)
        
        return request.Response(
            data=serializer,
            status=HTTP_200_OK
        )
