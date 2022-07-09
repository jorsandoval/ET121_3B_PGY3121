from django.urls import path
from rest_Usuario import listaUsuarios, detalleUsuario

urlpatterns = [
    path('listaUsuarios', listaUsuarios, name='listaUsuarios'),
    path('detalleUsuario', detalleUsuario, name='detalleUsuario'),
]