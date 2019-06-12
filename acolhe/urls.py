from django.contrib import admin
from django.urls import path
from .views import geral, anfitriao, acolhido

urlpatterns = [
   path('', geral.home),
   path('acolhido/', acolhido.home_acolhido, name = 'home_acolhido'),
   path('anfitriao/', anfitriao.home_anfitriao, name = 'home_anfitriao'),
]
