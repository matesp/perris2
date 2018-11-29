from rest_framework import serializers
from .models import Usuario, Rescatado

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('url', 'username', 'fechanacimiento', 'telefono', 'email', 'region', 'comuna', 'vivienda', 'password', 'is_active', 'is_staff')

class RescatadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rescatado
        fields = ('url', 'nombre', 'descripcion', 'raza', 'estado', 'foto')