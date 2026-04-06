from django.contrib import admin
from django.http import JsonResponse
from django.urls import path

from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/',GenreCreateListView.as_view() , name='genre-view'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='detail-view-genre')
]
    