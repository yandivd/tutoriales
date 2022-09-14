from django.urls import path
# from usuario.api.api import UsuarioAPIView
from usuario.api.api import user_api_view

urlpatterns = [
    # path('usuarios/', UsuarioAPIView.as_view(), name='usuario_api'),
    path('usuarios2/', user_api_view, name='usuario_api_view'),
]