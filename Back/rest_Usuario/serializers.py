from dataclasses import fields
from rest_framework import serializers
from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            "idUsuario",
            "nombre",
            "apellidos",
            "correo",
            "direccion",
            "telefono",
            "comuna",
            "provincia",
            "region",
            "rut",
            "isSuscrito",
            "fechaSuscrito",
            "isAdmin",
        ]
