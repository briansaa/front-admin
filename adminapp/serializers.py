from rest_framework import serializers

from .models import (Horario, Laboratorio, Pabellon, Polideportivo,
                     ReservaLaboratorio, ReservaPolideportivo, Usuario)


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'codigo','email', 'contrasena']

class PolideportivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polideportivo
        fields = ['id','nombre']

class PabellonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pabellon
        fields = ['id','nombre']

class LaboratorioSerializer(serializers.ModelSerializer):
    pabellones = PabellonSerializer(many=True, read_only=True)  # Incluye los Pabellones

    class Meta:
        model = Laboratorio
        fields = ['id','nombre', 'pabellones']

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = ['id','hora_inicio', 'hora_fin']
class ReservaLaboratorioSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()
    laboratorio = LaboratorioSerializer()

    class Meta:
        model = ReservaLaboratorio
        fields = ['id','laboratorio', 'fecha', 'Horario_inicio', 'Horario_fin', 'usuario']

class ReservaPolideportivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaPolideportivo
        fields = ['id','polideportivo', 'fecha', 'Horario', 'Usuario']
