from django import forms
from .models import Onibus, Linha, Rota

class RotaForm(forms.ModelForm):
    class Meta:
        model = Rota
        fields = ['nome']

class LinhaForm(forms.ModelForm):
    class Meta:
        model = Linha
        fields = ['numero', 'descricao']  # Adicione outros campos que você deseja incluir

class OnibusForm(forms.ModelForm):
    class Meta:
        model = Onibus
        fields = ['capacidade_sentados', 'numero', 'capacidade_em_pe']  # Verifique se esses campos existem no modelo
