from django.urls import path
from usuario.api.api import UsuarioAPIView

urlpatterns = [
    path('api1/', UsuarioAPIView.as_view(), name='usuario_api'),
]