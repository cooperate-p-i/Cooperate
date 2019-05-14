from django.urls import path

from apps.clientes.views import CreateCliente, ListCliente, DeleteCliente, UpdateCliente

urlpatterns = [

    path('novo', CreateCliente.as_view(), name = 'create_cliente'),
    path('', ListCliente.as_view(), name = 'list_cliente'),
    path('delete/<int:pk>', DeleteCliente.as_view(), name = 'delete_cliente'),
    path('update/<int:pk>', UpdateCliente.as_view(), name = 'update_cliente'),


]