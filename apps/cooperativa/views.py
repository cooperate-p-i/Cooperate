from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView

from apps.cooperativa.forms import formFuncionario
from apps.cooperativa.models import Funcionario


class CreateFuncionario(CreateView):
    model = Funcionario
    form_class = formFuncionario

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        funcionario.cooperativa = self.request.user.funcionario.cooperativa
        username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.usuario = User.objects.create(username=username)
        funcionario.save()
        return super(CreateFuncionario, self).form_valid(form)


