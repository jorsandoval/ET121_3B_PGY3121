from django.urls import path
from rest_Usuario import usuariosGetAll, usuarioById

urlpatterns = [
    path('usuarios/', usuariosGetAll, name='listaUsuarios'),
    path('usuarios/<idUsuario>', usuarioById, name='usuarioById'),
]