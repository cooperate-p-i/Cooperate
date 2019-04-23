from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from apps.pessoal.models import Membro, Familia


class CreateMembro(CreateView):
    model = Membro
    fields = ['nome', 'rg', 'cpf', 'dataDeNascimento', 'familia']

class CreateFamilia(CreateView):
    model = Familia
    fields = ['nome', 'dataDeCadastro', ]


