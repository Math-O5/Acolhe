from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import UserForm, AcolhidoLoginForm, Local, Anfitriao

def disponivel_view(request, id):
	Local.objects.filter(id=id).update(status="DISPONIVEL")
	Local.objects.filter(id=id).update(acolhido=None)
		
	return redirect('anfitriao:home_anfitriao')

def ocupado_view(request, id):
	Local.objects.filter(id=id).update(status="OCUPADO")
	Local.objects.filter(id=id).update(acolhido=request.user.acolhido)
	# Acolhido.objects.filter(name=request.user).achou_moradia = 1

	return redirect('acolhido:home_acolhido')

def cancelar_view(request, id):
	Local.objects.filter(id=id).update(status="DISPONIVEL")
	Local.objects.filter(id=id).update(acolhido=None)
		
	return redirect('acolhido:home_acolhido')