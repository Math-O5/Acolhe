from django.contrib import admin
from .models import User, Acolhido, Anfitriao, Local, Comment

admin.site.register(User)
admin.site.register(Acolhido)
admin.site.register(Anfitriao)
admin.site.register(Local)
admin.site.register(Comment)