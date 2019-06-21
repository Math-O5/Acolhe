from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserForm, AnfitriaoLoginForm, LocalForm
from ..models import Local, Anfitriao, User

# Create your views here.
def home_anfitriao(request):    
	local_disponivel = Local.objects.filter(anfitriao__nome=request.user.anfitriao.nome, status="DISPONIVEL")
	local_solicitado = Local.objects.filter(anfitriao__nome=request.user.anfitriao.nome, status="SOLICITADO")
	local_aprovado = Local.objects.filter(anfitriao__nome=request.user.anfitriao.nome, status="OCUPADO")

	context = {
		'local_disponivel': local_disponivel,
		'local_solicitado': local_solicitado,
		'local_aprovado': local_aprovado,
	}

	if request.user.is_authenticated and request.user.is_anfitriao:
		return render(request, "anfitriao/home.html", context)
		

def cadastrar_view(request):
    user_form = UserForm(request.POST or None)
    profile_form = AnfitriaoLoginForm(request.POST or None)

    if request.method == 'POST':
        user_form = UserForm(request.POST, prefix='UF')
        profile_form = AnfitriaoLoginForm(request.POST, prefix='PF')
		
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.is_anfitriao = True
            user.save()

            user.anfitriao.nome = profile_form.cleaned_data.get('nome')
            user.anfitriao.contato = profile_form.cleaned_data.get('contato')
            user.anfitriao.save()
                
            # log the user in
            login(request, user)
            return redirect('anfitriao:home_anfitriao')

    else:
        user_form = UserForm(prefix='UF')
        profile_form = AnfitriaoLoginForm(prefix='PF')
		
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'anfitriao_form.html', context)

def cadastrar_local_view(request):
	local_form = LocalForm(request.POST or None)

	if request.method == 'POST':
		local_form = LocalForm(request.POST)

		if local_form.is_valid():
			local = local_form.save(commit=False)
			local.anfitriao = request.user.anfitriao
			local.save()

			return redirect('anfitriao:home_anfitriao')
	else:
		local_form = LocalForm(None)

	context = {
		'local_form': local_form,
	}

	return render(request, 'local_form.html', context)

