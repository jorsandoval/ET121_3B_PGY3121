from django.urls import path
from rest_Auth.views import singUp, login

urlpatterns = [
    path('singUp', singUp, name='singUp'),
    path('login', login, name='login'),
]
