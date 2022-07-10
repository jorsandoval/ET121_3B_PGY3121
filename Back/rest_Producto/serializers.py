from dataclasses import fields
from rest_framework import serializers
from .models import Producto, Categoria, Promocion


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = [
            "idProducto",
            "nombre",
            "valor",
            "descripcion",
            "stock",
            "imagen",
            "categoria",
        ]


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = [
            "idCategoria",
            "nombreCategoria",
        ]


class PromocionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocion
        fields = [
            "idPromocion",
            "producto",
            "pordesct",
        ]
