from django import forms

from apps.cooperativa.models import Funcionario


class formFuncionario(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Funcionario
        fields = ['nome', 'matricula', 'usuario', 'senha']
