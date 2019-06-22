from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import UserForm, AcolhidoLoginForm, CommentForm, Local, Anfitriao, Acolhido, CommentForm
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

def detalhes_view(request, id):
    local = get_object_or_404(Local, id=id)

    return render(request, 'local_detalhe.html', {'local': local})

def add_comment_to_local(request, pk):
	local = get_object_or_404(Local, pk=pk)

	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.local = local
			comment.save()
			return redirect('detalhes_view', id=local.pk)
	else:
		form = CommentForm()
	return render(request, 'add_comment_to_local.html', {'form': form})
