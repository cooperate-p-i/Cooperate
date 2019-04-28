from django.forms import ModelForm

from apps.pessoal.models import Familia, Membro


class MembroForm(ModelForm):

    def __init__(self, id, *args, **kwargs):
        super(MembroForm, self).__init__(*args, **kwargs)
        self.fields['familia'].queryset = Familia.objects.filter(id = id)


    class Meta:
        model = Membro
        fields = ['nome', 'cpf', 'rg', 'dataDeNascimento', 'familia']