from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from ..models import Local
from django.utils import timezone
class cadastrarView(TemplateView):
   template_name = 'registrar/signup.html'

def home_view(request):
	local_disponivel = Local.objects.order_by('-publicado_date').filter(status="DISPONIVEL")[:3]
	timenow = timezone.now()

	context = {
		'local_disponivel': local_disponivel,
		'timenow': timenow,
	}
	return render(request, 'home.html', context)

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			# log the user in
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(username=username, password=password)
			login(request, user)
			
			if user.is_acolhido:
				return redirect('acolhido:home_acolhido')
			if user.is_anfitriao:
				return redirect('anfitriao:home_anfitriao')
	else:
		form = AuthenticationForm()
	return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')