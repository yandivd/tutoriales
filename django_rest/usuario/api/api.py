from rest_framework import status
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

    #listar
    if request.method == 'GET':
        #queryset
        usuarios = Usuario.objects.all()
        usuarios_serializer = UsuarioSerializer(usuarios, many=True)
        return Response(usuarios_serializer.data, status=status.HTTP_200_OK)

    #create
    elif request.method == 'POST':
        usuario_serializer = UsuarioSerializer(data=request.data)

        #validation 
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return Response(usuario_serializer.data, status=status.HTTP_201_CREATED)
        return Response(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def usuario_detail_api_view(request,id):
    #queryset
    user=Usuario.objects.get(id=id)

    #validacion
    if user:

        #retrieve
        if request.method == 'GET':
            usuario_serializer = UsuarioSerializer(user)
            return Response(usuario_serializer.data, status=status.HTTP_200_OK)

        #update
        elif request.method == 'PUT':
            usuario_serializer = UsuarioSerializer(user, data=request.data)
            if usuario_serializer.is_valid():
                usuario_serializer.save()
                return Response(usuario_serializer.data, status=status.HTTP_200_OK)
            return Response(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        #delete
        elif request.method == 'DELETE':
            user.delete()
            return Response({'message':'Usuario Eliminado Correctamente!'}, status=status.HTTP_200_OK)

    return Response({'message':'No se ha encontnrado un usuario con esos datos'}, status=status.HTTP_400_BAD_REQUEST)