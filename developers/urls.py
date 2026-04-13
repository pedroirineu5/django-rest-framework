from django.urls import path
from . import views

urlpattern = [
    path('developers/', views.DevelopersCreateClass.as_view(), name='developers_list'),
    path('developers/<int:pk>/', views.DevelopersDetailUpdateDestroyClass.as_view(),name='developers_detail'),
]