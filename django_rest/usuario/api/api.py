from rest_framework.response import Response
from rest_framework.views import APIView
from usuario.models import Usuario
from usuario.api.serializer import UsuarioSerializer

class UsuarioAPIView(APIView):
    def get(self, request):
        usuarios = Usuario.objects.all()
        usuarios_serializer = UsuarioSerializer(usuarios, many=True)
        
        return Response(usuarios_serializer.data)
