from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario
from .serializers import UsuarioSerializer

# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET','POST'])
#@permission_classes((IsAuthenticated,))
def usuariosGetAll(request):
    if request.method == 'GET':
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializer(usuario, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        data = JSONParser().parse(request)
        if type(data) == dict:
            usuario = UsuarioSerializer(data=data)
            if usuario.is_valid():
                usuario.save()
                return Response(usuario.data, status=status.HTTP_201_CREATED)
        else:
            for objUsuario in data:
                usuario = UsuarioSerializer(data=objUsuario)
                if usuario.is_valid():
                    usuario.save()
            return Response(usuario.data, status=status.HTTP_201_CREATED)

@csrf_exempt
@api_view(['GET','PUT','DELETE'])
#@permission_classes((IsAuthenticated,))
def usuarioById(request,idUsuario):
    """ 
    Get, update o delete de un Usuario en especifico.
    Recibe el parametro <idUsuario>
    """
    try:
        usuario = Usuario.objects.get(idUsuario=idUsuario)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(usuario, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)