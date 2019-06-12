from django.contrib import admin
from .models import Acolhido

@admin.register(Acolhido)
class AcolhidoAdmin(admin.ModelAdmin):
    pass