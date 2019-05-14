from builtins import super

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from django.views.generic.base import View

from apps.ambiental.forms import PropriedadeForm
from apps.ambiental.models import Propriedade, Cultura, Producao


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
        fields = ['nome', 'areaTotal','areaReserva','responsavel', 'proprietario']

@login_required
def homeAmbiental(request):
    data = {}
    data['usuario'] = request.user
    return render(request, 'ambiental/ambiental_index.html', data)


#Culturas
class ListCultura(ListView):
    model = Cultura

class CreateCultura(CreateView):
    model = Cultura
    fields = ['nome', 'tipo', 'areaPlantada', 'propriedade']

class UpdateCultura(CreateView):
    model = Cultura
    fields = ['nome', 'tipo', 'areaPlantada', 'propriedade']

#Rebanhos

class ListProducao(ListView):
    model = Producao

class CreateProducao(CreateView):
    model = Producao
    fields = ['tipo', 'quantidade', 'unidade']

class UpdateProducao(CreateView):
    model = Producao
    fields = ['tipo', 'quantidade', 'unidade']

