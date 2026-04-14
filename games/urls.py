from django.urls import path

from . import views

urlpatterns = [
    path('games/', views.GamesListCreateView.as_view(), name='games_list'),
    path('games/<int:pk>/', views.GamesRetrieveUpdateDestroyAPIView.as_view(), name="games_detail"),
]
