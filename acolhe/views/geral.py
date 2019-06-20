from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

class cadastrarView(TemplateView):
   template_name = 'registrar/signup.html'

def home_view(request):
	if request.user.is_authenticated:
       		if request.user.is_anfitriao:
            		return redirect('anfitriao:home_anfitriao')
        	else:
        	    return redirect('acolhido:home_acolhido')
	return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')