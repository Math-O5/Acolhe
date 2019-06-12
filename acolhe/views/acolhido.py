from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import AcolhidoRegistrar

# Create your views here.
def home_acolhido(request):
    if request.user.is_authenticated and request.user.is_acolhido:
        return render(request, "acolhido/home.html")

def cadastrar(request):
    if request.method == 'POST':
        form = AcolhidoRegistrar(request.POST)
        if form.is_valid():
            form.save()
            usuario = form.cleaned_data.get('nome')
            senha = form.cleaned_data.get('password1') 
            user = authenticate(username=usuario, password=senha)
            login(request, user)
            return render(request, 'acolhido/home.html')
    return render(request, "registrar/signup_acolhido.html")
