from django.contrib import admin
from django.urls import path, include
from acolhe.views import geral, acolhido, anfitriao

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('acolhe.urls')),
#    path('perfil/', include('django.contrib.auth.urls')),
]
