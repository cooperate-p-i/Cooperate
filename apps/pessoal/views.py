from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


from apps.pessoal.models import Membro, Familia


class CreateFamilia(CreateView):
    model = Familia
    fields = ['nome', 'dataDeCadastro', ]

    def form_valid(self, form):
        familia = form.save(commit = False)

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


class CreateMembro(CreateView):
    model = Membro
    fields = ['nome', 'rg', 'cpf', 'dataDeNascimento']

    def form_valid(self, form):
        import pdb; pdb.set_trace()
        membro = form.save(commit=False)
        membro.familia = self.objects.all()

        return super(CreateMembro, self).form_valid(form)


class ListMembro(ListView):
    model = Membro

    def get_queryset(self):

        qs = self.kwargs.get('familia_id')
        queryset = Membro.objects.filter(familia_id=qs)
        return queryset




