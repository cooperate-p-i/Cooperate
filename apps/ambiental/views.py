from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView

from apps.ambiental.forms import PropriedadeForm
from apps.ambiental.models import Propriedade


class CreatePropriedade(CreateView):
    model = Propriedade
    form_class = PropriedadeForm

    def get_form_kwargs(self):
        kwargs = super(CreatePropriedade, self).get_form_kwargs()
        kwargs.update({'id': self.kwargs.get('familia_id')})
        return kwargs




class ListPropriedade(ListView):
    model = Propriedade






class DetailPropriedade(DetailView):

    queryset = Propriedade.objects.all()

    def get_object(self):
        obj = super().get_object()
        obj.last_accessed = timezone.now()
        obj.save()
        return obj




class UpdatePropriedade(UpdateView):
        model = Propriedade
        fields = ['nome', 'areaTotal','areaReserva','responsavel', 'proprietario', 'culturaPrimaria', 'rebanho1']