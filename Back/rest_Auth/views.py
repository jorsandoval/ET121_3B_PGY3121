from dataclasses import dataclass
from msilib.schema import ServiceInstall
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer


# Create your views here.
@api_view(['POST'])
def singUp(request):
    data = JSONParser().parse(request)
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)
    try:
        user = User.objects.get(username=data["username"])
    except User.DoesNotExist:
        return Response("Usuario no se encuentra en los registros")
    
    pass_valido = check_password(data["password"], user.password)
    if not pass_valido:
        return Response("Contraseña incorrecta, intente nuevamente.")
    token, create = Token.objects.get_or_create(user=user)
    return Response(token.key)