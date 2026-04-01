import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
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
    
    # OPERAÇÃO COM O ORM
    genre = get_object_or_404(Genre, pk=pk)

    if request.method == 'GET':
        data = {'id': genre.id,'name':genre.name}
        return JsonResponse(data)
    
    elif request.method == 'PUT':

        # convertendo os usuarios a usarem o melhor 
        data_user_put = json.loads(request.body.decode('utf-8'))
        genre.name = data_user_put['name']
        genre.save()
        
        return JsonResponse(
            {
                'id': genre.id,
                'name': genre.name
            }
        ) 
    
    if request.method == 'DELETE':
        genre.delete()
        JsonResponse(
            {"Message" : "The Data has been delete successfully!"}
        )