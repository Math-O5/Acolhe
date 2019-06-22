from django import forms
from django.contrib.auth.forms import UserCreationForm
from ..models import Acolhido, User, Anfitriao, Local, Comment

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'foto')

class AcolhidoLoginForm(forms.ModelForm):
    class Meta:
        model = Acolhido
        fields = ('nome', 'contato', 'descricao', 'vagas')

class AnfitriaoLoginForm(forms.ModelForm):
    class Meta:
        model = Anfitriao
        fields = ('nome', 'contato')

class LocalForm(forms.ModelForm):
	class Meta:
		model = Local
		fields = ('cidade', 'bairro', 'rua', 'numero', 'vagas', 'descricao', 'status', 'foto')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)