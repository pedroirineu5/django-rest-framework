from django.urls import path

from . import views

urlpatterns = [
    path('platforms/',views.PlatformCreateView.as_view(),name='platforms_list' ),
    path('platforms/<int:pk>/',views.PlatformRetrieveUpdateDestroyAPIView.as_view(), name='platforms_detail'),
]