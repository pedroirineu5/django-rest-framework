from django.urls import path
from . import views

urlpatterns = [

    path('review/', views.ReviewCreate.as_view(), name='review_list'),
    path('review/<int:pk>/', views.ReviewRetrieveUpdateDestroy.as_view(), name='review_detail'),
]