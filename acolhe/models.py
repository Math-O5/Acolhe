from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_acolhido = models.BooleanField('acolhido_user', default=False)
    is_anfitriao = models.BooleanField('anfitriao_user', default=False)

class Acolhido(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nome = models.CharField(max_length=120)
    contato = models.CharField(max_length=11)
    descricao = models.TextField()
    vagas = models.PositiveIntegerField(default=1)
    achou_moradia = models.BooleanField(default=False)
    # fotinha
    # email