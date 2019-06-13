from django.contrib import admin
from django.urls import path
from acolhe.views import geral, anfitriao, acolhido

urlpatterns = [
   path('', geral.home_view, name='home'),
   path('acolhido/', acolhido.home_acolhido, name = 'home_acolhido'),
   path('anfitriao/', anfitriao.home_anfitriao, name = 'home_anfitriao'),
   path('acolhido/cadastrar', acolhido.cadastrar_view, name='cadastrar_acolhido'),
   path('anfitriao/cadastrar', anfitriao.cadastrar_view, name='cadastrar_anfitriao'),
   path('login/', geral.login_view, name='login'),
   path('logout/', geral.logout_view, name='logout'),
]
