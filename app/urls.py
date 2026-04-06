from django.contrib import admin
from django.http import JsonResponse
from django.urls import path

from developers.views import (DevelopersCreateClass,
                              DevelopersDetailUpdateDestroyClass)
from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/',GenreCreateListView.as_view() , name='genre-view'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='detail-view-genre'),
    path('developers/', DevelopersCreateClass.as_view(), name='developers-view'),
    path('developers/<int:pk>/', DevelopersDetailUpdateDestroyClass.as_view(),name='Detail_view')
]
    