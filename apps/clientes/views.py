from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView

from apps.clientes.models import Cliente


class CreateCliente(CreateView):
    model = Cliente
    fields = ['nome', 'cnpj', 'endereco' ]

    def form_valid(self, form):
        cliente = form.save(commit = False)
        cliente.cooperativa = self.request.user.funcionario.cooperativa

        cliente.save()
        return super(CreateCliente, self).form_valid(form)

class DeleteCliente(DeleteView):
    model = Cliente

    success_url = reverse_lazy('list_cliente')

class UpdateCliente(UpdateView):
    model = Cliente
    fields = ['nome','cnpj','endereco']


class ListCliente(ListView):
    model = Cliente

    def get_queryset(self):
        cooperativa_logada = self.request.user.funcionario.cooperativa
        queryset = Cliente.objects.filter(cooperativa=cooperativa_logada)
        return queryset
