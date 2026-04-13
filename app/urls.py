from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),

    path('api/v1/', include('genres.urls')),

    path('api/v1/', include('developers.urls')),

    path('api/v1/', include('platforms.urls')),

    path('api/v1/', include('publisher.urls')),
    
    path('api/v1/', include('games.urls')),

    path('api/v1/', include('reviews.urls'))
]
    