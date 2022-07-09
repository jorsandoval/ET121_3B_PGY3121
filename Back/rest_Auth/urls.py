from django.urls import path
from rest_Auth.views import singUp

urlpatterns = [
    path('singUp', singUp, name='singUp'),
]
