from django import forms
from django.contrib.auth.forms import UserCreationForm
from ..models import Acolhido

class AcolhidoRegistrar(UserCreationForm):
    nome = Acolhido.nome
    # models.CharField(max_length=120, help_text="Nome inteiro")
    contato = Acolhido.contato
    # models.CharField(max_length=11, help_text="Deixe seu contato para ser ajudado.")
    descricao = Acolhido.descricao
    # models.TextField(help_text="Deixe um texto da sua história.")
    vagas = Acolhido.vagas
    # models.PositiveIntegerField(default=1, help_text="Quantas vagas necessito.")

    class Meta:
        model = Acolhido
        fields = ('nome', 'contato', 'vagas', 'descricao', 'password1', 'password2')
