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
        #validar que ningun usuario se llame Yandi
        if 'Yandia' in value:
            print('HAHAAAH')
            raise serializers.ValidationError('Error, ninguna persona se puede llamar asi')
        print(value)
        return value

    def validate_email(self,value):
        #validar q el correo no este vacio
        if value == '':
            raise serializers.ValidationError('Error, el correo no puede estar en blanco')
        # if self.validate_name(self.context['name']) in value:
        #     raise serializers.ValidationError('El nombre no puede estar contenido en el correo')
        print(value)
        return value

    def validate(self, data):
        print('Validate General')
        # if data['name'] in data['email']:
        #     raise serializers.ValidationError('Error, el correo no puede contener el nombre')
        return data

    def create(self, validated_data):
        print(validated_data)
        return Usuario(**validated_data)