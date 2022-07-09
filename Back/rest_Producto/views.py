from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.request import HttpRequest
from rest_framework.parsers import JSONParser

from .models import Producto, Promocion, Categoria
from .serializers import ProductoSerializer, CategoriaSerializer, PromocionSerializer

# Create your views here.
"""

    Productos

"""


@api_view(["GET", "POST"])
def productGetAll(request: HttpRequest):
    if request.method == "GET":
        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        data = JSONParser().parse(request)
        producto = ProductoSerializer(data=data)
        if producto.is_valid():
            producto.save()
            return Response(producto.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def productById(request: HttpRequest, id: int):
    try:
        producto: Producto = Producto.objects.get(idProducto=id)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ProductoSerializer(producto)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(producto, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        producto.delete()
        return Response(status=status.HTTP_200_OK)


"""

    Categorias

"""


@api_view(["GET", "POST"])
def categoriaGetAll(request: HttpRequest):
    if request.method == "GET":
        categorias: Categoria = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        data = JSONParser().parse(request)
        categoria = CategoriaSerializer(data=data)
        if categoria.is_valid():
            categoria.save()
            return Response(categoria.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def categoriaById(request: HttpRequest, id: int):
    try:
        categoria: Categoria = Categoria.objects.get(idCategoria=id)
    except Categoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = CategoriaSerializer(categoria, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        categoria.delete()
        return Response(status=status.HTTP_200_OK)


"""

    Promocion

"""


@api_view(["GET", "POST"])
def promocionGetAll(request: HttpRequest):
    if request.method == "GET":
        promocion: Promocion = Promocion.objects.all()
        serializer = PromocionSerializer(promocion, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        data = JSONParser().parse(request)
        promocion = PromocionSerializer(data=data)
        if promocion.is_valid():
            promocion.save()
            return Response(promocion.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def promocionById(request: HttpRequest, id: int):
    try:
        promocion: Promocion = Promocion.objects.get(idPromocion=id)
    except Promocion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = PromocionSerializer(promocion)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = PromocionSerializer(promocion, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        promocion.delete()
        return Response(status=status.HTTP_200_OK)
