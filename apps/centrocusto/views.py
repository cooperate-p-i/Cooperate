from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView,DeleteView
from apps.centrocusto.models import Centrocusto

class ListCentroDeCustos(ListView):

    model = Centrocusto


class CreateCentroCusto(CreateView):
    model = Centrocusto

    fields = ['nome', 'descricao']

class UpdateCentroCusto(UpdateView):
    model = Centrocusto
    fields = ['nome', 'descricao']

class DeleteCentroCusto(DeleteView):
    model = Centrocusto
    success_url = reverse_lazy('list_centrocusto')