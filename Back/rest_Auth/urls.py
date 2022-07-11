from django.urls import path
from rest_Auth.views import singUp, login, changePassword
from .views import usuariosGetAll, usuarioById

urlpatterns = [
    path("singUp", singUp, name="singUp"),
    path("login", login, name="login"),
    path("changePassword", changePassword, name="changePassword"),
    path('usuarios/', usuariosGetAll, name='usuariosGetAll'),
    path('usuarios/<idUsuario>', usuarioById, name='usuarioById'),
]
