from django.db import models
from rest_Producto.models import Producto

# Create your models here.
class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True, verbose_name="id de producto")
    nombre = models.CharField(max_length=255, null=False, verbose_name="Nombre de producto")
    valor = models.IntegerField(null=False, verbose_name="Valor de producto")
    descripcion = models.CharField(max_length=255,null=False, verbose_name="Descripcion de producto")
    stock = models.IntegerField(null=False, default=0, verbose_name="Stock de producto")
    imagen = models.CharField(max_length=512, null=False, verbose_name="Imagen de producto")

class Promocion(models.Model):
    idPromocion = models.AutoField(primary_key=True, verbose_name="id promocion")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")
    pordesct = models.IntegerField(max_length=3, null=False, verbose_name="porcentaje de descuento")
    