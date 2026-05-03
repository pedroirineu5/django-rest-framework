from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

## TODO  continuar com auth jwt

urlpatterns=[
    path('authentication/token/', TokenObtainPairView.as_view(), name='token_obtain_pair')
]
