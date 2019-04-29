
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView


from apps.pessoal.forms import MembroForm
from apps.pessoal.models import Membro, Familia


class CreateFamilia(CreateView):
    model = Familia
    fields = ['nome', 'dataDeCadastro', ]

    def form_valid(self, form):
        familia = form.save(commit = False)
        familia.cooperativa = self.request.user.funcionario.cooperativa

        familia.save()
        return super(CreateFamilia, self).form_valid(form)

class DeleteFamilia(DeleteView):
    model = Familia

    success_url = reverse_lazy('list_familia')

class UpdateFamilia(UpdateView):
    model = Familia
    fields = ['nome']


class ListFamilia(ListView):
    model = Familia

    def get_queryset(self):
        cooperativa_logada = self.request.user.funcionario.cooperativa
        queryset = Familia.objects.filter(cooperativa=cooperativa_logada)
        return queryset


class CreateMembro(CreateView):
    model = Membro
    form_class = MembroForm

    def get_form_kwargs(self):
        kwargs = super(CreateMembro, self).get_form_kwargs()
        kwargs.update({'id': self.kwargs.get('familia_id')})
        return kwargs




class ListMembro(ListView):
    model = Membro

    def get_queryset(self):

        qs = self.kwargs.get('familia_id')
        queryset = Membro.objects.filter(familia_id=qs)
        return queryset




class DetailMembro(DetailView):

    queryset = Membro.objects.all()

    def get_object(self):
        obj = super().get_object()
        obj.last_accessed = timezone.now()
        obj.save()
        return obj
