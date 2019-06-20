from django.contrib import admin
from django.urls import path, include
from acolhe.views import geral, anfitriao, acolhido

urlpatterns = [
   path('', geral.home_view, name='home'),
   path('acolhido/', include(([
      path('', acolhido.home_acolhido, name = 'home_acolhido'),
      path('cadastrar', acolhido.cadastrar_view, name='cadastrar_acolhido'),
   ], 'acolhe'), namespace='acolhido')
   ),


   path('anfitriao/', include(([
      path('', anfitriao.home_anfitriao, name = 'home_anfitriao'),
      path('cadastrar', anfitriao.cadastrar_view, name='cadastrar_anfitriao'),
      path('local', anfitriao.cadastrar_local_view, name='cadastrar_local'),
   ], 'acolhe'),namespace='anfitriao')
   ),
   
   path('login/', geral.login_view, name='login'),
   path('logout/', geral.logout_view, name='logout'),
]