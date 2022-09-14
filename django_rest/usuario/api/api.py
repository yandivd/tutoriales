from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from usuario.models import Usuario
from usuario.api.serializer import UsuarioSerializer

# class UsuarioAPIView(APIView):
#     def get(self, request):
#         usuarios = Usuario.objects.all()
#         usuarios_serializer = UsuarioSerializer(usuarios, many=True)
        
#         return Response(usuarios_serializer.data)

@api_view(['GET', 'POST'])
def user_api_view(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        usuarios_serializer = UsuarioSerializer(usuarios, many=True)
        
        return Response(usuarios_serializer.data)
    elif request.method == 'POST':
        print(request.data)
