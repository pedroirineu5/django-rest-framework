from django.contrib import admin
from django.http import JsonResponse
from django.urls import path

from genres.views import detail_view_genre, genre_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', genre_view, name='genre-view'),
    path('genres/<int:pk>/', detail_view_genre, name='detail-view-genre')
]
    