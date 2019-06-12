from django.shortcuts import redirect, render
from django.views.generic import TemplateView

class cadastrarView(TemplateView):
   template_name = 'registrar/signup.html'

def home(request):
	if request.user.is_authenticated:
       		if request.user.is_anfitriao:
            		return redirect('anfitriao:home_anfitriao')
        	else:
        	    return redirect('acolhido:home_acolhido')
	return render(request, 'home.html')
