from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def hello_world(request):
    return JsonResponse({'message':'hello world'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world)
]
