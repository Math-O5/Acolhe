from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserForm, AcolhidoLoginForm

# Create your views here.
def home_acolhido(request):
    if request.user.is_authenticated and request.user.is_acolhido:
        return render(request, "acolhido/home.html")

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
            return redirect('home')

    else:
        user_form = UserForm(prefix='UF')
        profile_form = AcolhidoLoginForm(prefix='PF')
		
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'acolhido_form.html', context)