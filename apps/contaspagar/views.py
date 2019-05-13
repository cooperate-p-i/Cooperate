from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from apps.contaspagar.forms import ContasPagarForm
from apps.contaspagar.models import ContasPagar
from apps.pessoal.models import Familia


class CreateContasPagar(CreateView):
    model = ContasPagar
    form_class = ContasPagarForm

    def get_form_kwargs(self):
        kwargs = super(CreateContasPagar, self).get_form_kwargs()
        kwargs.update({'id': self.kwargs.get('familia_id')})
        return kwargs

    def form_valid(self, form):
        contas = form.save(commit=False)
        cooperativa_logada = self.request.user.funcionario.cooperativa
        contas.cooperativa = cooperativa_logada
        contas.save()

        return super(CreateContasPagar, self).form_valid(form)



class ListContasPagar(ListView):
    model = ContasPagar

    def get_queryset(self):
        qs = self.kwargs.get('familia_id')
        queryset = ContasPagar.objects.filter(familia_id=qs)
        return queryset

@login_required
def select(request):
    data = {}
    data['usuario'] = request.user
    return render(request, 'contaspagar/contaspagar_familia_list.html', data)


class DetailContaPagar(DetailView):
    queryset = ContasPagar.objects.all()

    def get_object(self):
        obj = super().get_object()
        obj.last_accessed = timezone.now()
        obj.save()
        return obj
