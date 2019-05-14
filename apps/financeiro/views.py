
from django.views.generic import CreateView, ListView
from apps.financeiro.models import Orcamento, Rentabilidade

class ListOrcamento(ListView):
    model = Orcamento

class CreateOrcamento(CreateView):
    model = Orcamento
    fields = ['producao', 'valor']

class UpdateOrcamento(CreateView):
    model = Orcamento
    fields = ['producao', 'valor']

#------------------#
class ListRentabilidade(ListView):
    model = Orcamento

class CreateRentabilidade(CreateView):
    model = Rentabilidade
    fields = ['producao', 'data', 'valor']

class UpdateRentabilidade(CreateView):
    model = Rentabilidade
    fields = ['producao', 'data', 'valor']