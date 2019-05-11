from django import forms

from apps.centrocusto.models import Centrocusto


class formCentrocusto(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Centrocusto
        fields = ['nome','descricao']