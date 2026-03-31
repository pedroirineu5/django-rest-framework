import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from genres.models import Genre


# fazendo no braço para entender tudo
@csrf_exempt
def genre_view(request):

    if request.method == 'GET':
            
        genres = Genre.objects.all()

        data = []
        for genre in genres:
            data.append(
                {
                    'id': genre.id,
                    'name': genre.name
                }
            )
        return JsonResponse(data, safe=False)
    
    if request.method == 'POST':

        data_user = json.loads(request.body.decode('utf-8'))
        new_genre = Genre(name=data_user['name'])
        new_genre.save()
        
        return JsonResponse(
            {
                'id': new_genre.id,
                'name': new_genre.name
            },
            status = 201,
        )

@csrf_exempt
def detail_view_genre(request,pk):
    
    genre = Genre.objects.get(pk=pk)
