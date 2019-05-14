from django.urls import path

from .views import CreateContasPagar,ListContasPagar, select,DetailContaPagar, ExportarExcel

urlpatterns = [

    path('create/<int:familia_id>', CreateContasPagar.as_view(), name = 'create_conta_pagar'),
    path('list/<int:familia_id>', ListContasPagar.as_view(), name = 'list_conta_pagar'),
    path('select', select, name = 'select'),
    path('detalhes/<int:pk>', DetailContaPagar.as_view(), name = 'detail_conta_pagar'),
    path('relatorio-contas-a-pagar>', ExportarExcel.as_view(), name = 'relatorio_conta_pagar'),




]