from django.shortcuts import render

# Create your views here.
def home_anfitriao(request):    
    if request.user.is_authenticated and request.user.is_anfitriao:
        return render(request, "anfitriao/home.html")

def cadastrar(request):
    return render(request, "registrar/signup_anfitriao.html")
