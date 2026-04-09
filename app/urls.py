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
from reviews.views import ReviewCreate, ReviewRetrieveUpdateDestroy

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('genres/',GenreCreateListView.as_view() , name='genres_list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genres_detail'),
    path('developers/', DevelopersCreateClass.as_view(), name='developers_list'),
    path('developers/<int:pk>/', DevelopersDetailUpdateDestroyClass.as_view(),name='developers_detail'),
    path('platforms/',PlatformCreateView.as_view(),name='platforms_list' ),
    path('platforms/<int:pk>/',PlatformRetrieveUpdateDestroyAPIView.as_view(), name='platforms_detail'),
    path('publisher/',PublisherCreateListView.as_view(),name='publisher_list'),
    path('publisher/<int:pk>/', PublisherRetrieveUpdateDestroyAPIView.as_view(), name='publisher_detail'),
    path('games/', GamesListCreateView.as_view(), name='games_list'),
    path('games/<int:pk>/', GamesRetrieveUpdateDestroyAPIView.as_view(), name="games_detail"),
    path('review/', ReviewCreate.as_view(), name='review_list'),
    path('review/<int:pk>', ReviewRetrieveUpdateDestroy.as_view(), name='review_detail'),
]
    