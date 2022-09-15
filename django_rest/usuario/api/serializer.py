from rest_framework import serializers
from usuario.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class TestUsuarioSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()

    def validate_name(self,value):
        print(value)
        return value
    def validate_email(self,value):
        print(value)
        return value
    def validate(self, data):
        print('Validate General')
        return data