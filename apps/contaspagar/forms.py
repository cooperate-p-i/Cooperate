from django.forms import ModelForm

from apps.contaspagar.models import ContasPagar
from apps.pessoal.models import Familia


class ContasPagarForm(ModelForm):

    def __init__(self, id, *args, **kwargs):
        super(ContasPagarForm, self).__init__(*args, **kwargs)
        self.fields['familia'].queryset = Familia.objects.filter(id = id)




    class Meta:
        model = ContasPagar
        fields = ['nome', 'descricao', 'parcela_atual', 'data_documento', 'data_pagar', 'centrocusto',
                  'familia', 'valor', 'numero_parcela', 'numero_parcela_total', 'status' ]