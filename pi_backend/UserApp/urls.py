from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtener token de acceso
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Renovar token de acceso
    path('register/',RegisterView.as_view(),name='register'), #vista para crear usuarios
]