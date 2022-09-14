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
        usuario_serializer = UsuarioSerializer(data=request.data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return Response(usuario_serializer.data)
        return Response(usuario_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def usuario_detail_api_view(request,id):

    if request.method == 'GET':
        if id is not None:
            user=Usuario.objects.get(id=id)
            usuario_serializer = UsuarioSerializer(user)
            return Response(usuario_serializer.data)
    elif request.method == 'PUT':
        user=Usuario.objects.get(id=id)
        usuario_serializer = UsuarioSerializer(user, data=request.data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return Response(usuario_serializer.data)
        else:
            return Response(usuario_serializer.errors)
    elif request.method == 'DELETE':
        user=Usuario.objects.get(id=id)
        user.delete()
        return Response('Eliminado')