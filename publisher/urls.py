from django.urls import path

from . import views

urlpatterns = [
    path('platforms/',views.PublisherCreateListView.as_view(),name='platforms_list' ),
    path('platforms/<int:pk>/',views.PublisherRetrieveUpdateDestroyAPIView.as_view(), name='platforms_detail'),
]