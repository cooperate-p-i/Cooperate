from django.forms import ModelForm

from apps.ambiental.models import Propriedade
from apps.pessoal.models import Familia, Membro


class PropriedadeForm(ModelForm):

    def __init__(self, id, *args, **kwargs):
        super(PropriedadeForm, self).__init__(*args, **kwargs)
        self.fields['proprietario'].queryset = Familia.objects.filter(id = id)
        self.fields['responsavel'].queryset = Membro.objects.filter(familia_id= id)



    class Meta:
        model = Propriedade
        fields = ['nome', 'areaTotal','areaReserva','responsavel', 'proprietario', 'culturaPrimaria', 'rebanho1']


