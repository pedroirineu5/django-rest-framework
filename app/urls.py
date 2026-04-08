from django.contrib import admin
from django.http import JsonResponse
from django.urls import path

from developers.views import (DevelopersCreateClass,
                              DevelopersDetailUpdateDestroyClass)
from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView
from publisher.views import (PublisherCreateListView,
                             PublisherRetrieveUpdateDestroyAPIView)
from platforms.models import Pla

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/',GenreCreateListView.as_view() , name='genres-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genres-detail'),
    path('developers/', DevelopersCreateClass.as_view(), name='developers-list'),
    path('developers/<int:pk>/', DevelopersDetailUpdateDestroyClass.as_view(),name='developers-detail'),
    path('platforms/', ),
    path('platforms/<int:pk>/',),
    path('publisher/',PublisherCreateListView.as_view(),name='publisher-list'),
    path('publisher/<int:pk>/', PublisherRetrieveUpdateDestroyAPIView.as_view(), name='publisher-detail')
]
    