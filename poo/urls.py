from django.contrib import admin
from django.urls import path, include
from acolhe.views import geral, acolhido, anfitriao

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('acolhe.urls')),
   path('perfil/', include('django.contrib.auth.urls')),
   path('perfil/cadastrar/', geral.cadastrarView.as_view(), name='cadastrar'),
   path('perfil/cadastrar/dar_ajuda', anfitriao.cadastrar, name='cadastrar_anfitriao'),
   path('perfil/cadastrar/receber_ajuda', acolhido.cadastrar, name='cadastrar_acolhido'),
]
