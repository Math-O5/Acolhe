from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    is_anfitriao = models.BooleanField('anfitriao user', default=False)
    is_acolhido = models.BooleanField('acolhido user', default=False)

class Acolhido(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='acolhido')
    nome = models.CharField(max_length=120)
    contato = models.CharField(max_length=11)
    descricao = models.TextField()
    vagas = models.PositiveIntegerField(default=1)
    achou_moradia = models.BooleanField(default=False)
	# fotinha
    # email

class Anfitriao(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='anfitriao')
    nome = models.CharField(max_length=120)
    contato = models.CharField(max_length=11)
    local = models.
    # fotinha
    # email

class Local(models.Model):
	# anfitriao foreign key
	cidade = models.CharField(max_length=120)
	bairro = models.CharField(max_length=120)
	rua = models.CharField(max_length=120)
	numero = models.PositiveIntegerField()
	vagas = models.PositiveIntegerField(default=1)
	descricao = models.TextField()
	status_list = [("OCUPADO", 'ocupado'), ("DISPONIVEL", 'disponível')]
	status = models.CharField(max_length=20, choices=status_list, default="DISPONIVEL")
	# fotinha
	# inicio_estadia
	# termino_estadia
	# tipo

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	print('****', created)
	if instance.is_acolhido:
		Acolhido.objects.get_or_create(user = instance)
	elif instance.is_anfitriao:
		Anfitriao.objects.get_or_create(user = instance)
    
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	print('_-----')	
	# print(instance.internprofile.bio, instance.internprofile.location)
	if instance.is_acolhido:
		instance.acolhido.save()
	if instance.is_anfitriao:
		instance.anfitriao.save()