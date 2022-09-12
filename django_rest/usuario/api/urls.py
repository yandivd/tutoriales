from django.urls import path
from usuario.api.api import UsuarioAPIView

urlpatterns = [
    path('', UsuarioAPIView.as_view(), name='usuario_api'),
]