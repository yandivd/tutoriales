from django.urls import path
from usuario.api.api import UsuarioAPIView

urlpatterns = [
    path('usuarios/', UsuarioAPIView.as_view(), name='usuario_api'),
]