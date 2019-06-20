from django.contrib import admin
from django.urls import path
from acolhe.views import geral, anfitriao, acolhido, local

urlpatterns = [
   path('', geral.home_view, name='home'),
   path('acolhido/', acolhido.home_acolhido, name = 'home_acolhido'),
   path('acolhido/cadastrar', acolhido.cadastrar_view, name='cadastrar_acolhido'),

   path('anfitriao/', anfitriao.home_anfitriao, name = 'home_anfitriao'),
   path('anfitriao/cadastrar', anfitriao.cadastrar_view, name='cadastrar_anfitriao'),
   path('anfitriao/local', anfitriao.cadastrar_local_view, name='cadastrar_local'),

   path('local/<int:id>/ocupado', local.ocupado_view, name='local_ocupado'),
   path('local/<int:id>/cancelar', local.cancelar_view, name='local_cancelar'),
   path('local/<int:id>/disponivel', local.disponivel_view, name='local_disponivel'),
   
   path('login/', geral.login_view, name='login'),
   path('logout/', geral.logout_view, name='logout'),
]
