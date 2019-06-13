from django import forms
from django.contrib.auth.forms import UserCreationForm
from ..models import Acolhido, User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username',)

class AcolhidoLoginForm(forms.ModelForm):
    class Meta:
        model = Acolhido
        fields = ('nome', 'contato', 'descricao', 'vagas')

