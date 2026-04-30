from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),

    path('api/v1/', include('genres.urls')),

    path('api/v1/', include('developers.urls')),

    path('api/v1/', include('platforms.urls')),

    path('api/v1/', include('publisher.urls')),
    
    path('api/v1/', include('games.urls')),

    path('api/v1/', include('reviews.urls'))
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('')
]
    