from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import UserForm, AcolhidoLoginForm, Local, Anfitriao

# Create your views here.
def home_acolhido(request):
	local_disponivel = Local.objects.filter(status="DISPONIVEL")
	local_solicitado = Local.objects.filter(acolhido=request.user.acolhido)

	if request.GET.get('search'):
		search = request.GET.get('search')
		local_disponivel = Local.objects.filter(status="DISPONIVEL", cidade=search) 

	context = {
		'local_disponivel': local_disponivel,
		'local_solicitado': local_solicitado,
	}

	if request.user.is_authenticated and request.user.is_acolhido:
		return render(request, "acolhido/home.html", context)

def cadastrar_view(request):
    user_form = UserForm(request.POST or None)
    profile_form = AcolhidoLoginForm(request.POST or None)

    if request.method == 'POST':
        user_form = UserForm(request.POST, prefix='UF')
        profile_form = AcolhidoLoginForm(request.POST, prefix='PF')
		
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.is_acolhido = True
            user.save()

            user.acolhido.nome = profile_form.cleaned_data.get('nome')
            user.acolhido.contato = profile_form.cleaned_data.get('contato')
            user.acolhido.descricao = profile_form.cleaned_data.get('descricao')
            user.acolhido.vagas = profile_form.cleaned_data.get('vagas')
            user.acolhido.save()
                
            # log the user in
            login(request, user)
            return redirect('acolhido:home_acolhido')

    else:
        user_form = UserForm(prefix='UF')
        profile_form = AcolhidoLoginForm(prefix='PF')
		
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'acolhido_form.html', context)
