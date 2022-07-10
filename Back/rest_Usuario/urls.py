from django.urls import path
from .views import usuariosGetAll, usuarioById

urlpatterns = [
    path('usuarios/', usuariosGetAll, name='usuariosGetAll'),
    path('usuarios/<idUsuario>', usuarioById, name='usuarioById'),
]