from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import UserForm, AcolhidoLoginForm, Local, Anfitriao, Acolhido

def disponivel_view(request, id):
	Local.objects.filter(id=id).update(status="DISPONIVEL")
	Local.objects.filter(id=id).update(acolhido=None)
		
	return redirect('anfitriao:home_anfitriao')

def solicitar_view(request, id):
	Local.objects.filter(id=id).update(status="SOLICITADO")
	Local.objects.filter(id=id).update(acolhido=request.user.acolhido)

	return redirect('acolhido:home_acolhido')

def aprovar_view(request, id):
	local = Local.objects.filter(id=id)
	local.update(status="OCUPADO")
	acolhido = local.first().acolhido
	Acolhido.objects.filter(id=acolhido.id).update(achou_moradia=True)

	return redirect('anfitriao:home_anfitriao')

def cancelar_view(request, id):
	Local.objects.filter(id=id).update(status="DISPONIVEL")
	Local.objects.filter(id=id).update(acolhido=None)
		
	return redirect('acolhido:home_acolhido')