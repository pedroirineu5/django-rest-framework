from django.contrib import admin
from django.urls import path

from developers.views import (DevelopersCreateClass,
                              DevelopersDetailUpdateDestroyClass)
from games.views import GamesListCreateView, GamesRetrieveUpdateDestroyAPIView
from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView
from platforms.views import (PlatformCreateView,
                             PlatformRetrieveUpdateDestroyAPIView)
from publisher.views import (PublisherCreateListView,
                             PublisherRetrieveUpdateDestroyAPIView)

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('genres/',GenreCreateListView.as_view() , name='genres-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genres-detail'),
    path('developers/', DevelopersCreateClass.as_view(), name='developers-list'),
    path('developers/<int:pk>/', DevelopersDetailUpdateDestroyClass.as_view(),name='developers-detail'),
    path('platforms/',PlatformCreateView.as_view(),name='platforms-list' ),
    path('platforms/<int:pk>/',PlatformRetrieveUpdateDestroyAPIView.as_view(), name='platforms-detail'),
    path('publisher/',PublisherCreateListView.as_view(),name='publisher-list'),
    path('publisher/<int:pk>/', PublisherRetrieveUpdateDestroyAPIView.as_view(), name='publisher-detail'),
    path('games/', GamesListCreateView.as_view(), name='game-list'),
    path("games/<int:pk>/", GamesRetrieveUpdateDestroyAPIView.as_view(), name="game-detail")
]
    