from django.urls import path

from .views import CreateOrcamento, ListOrcamento, UpdateOrcamento, CreateRentabilidade, ListRentabilidade, UpdateRentabilidade

urlpatterns = [

path('list', ListOrcamento.as_view(), name='list_orcamento'),
path('create', CreateOrcamento.as_view(), name='create_orcamento'),
path('update/<int:pk>', UpdateOrcamento.as_view(), name='update_orcamento'),

path('list', ListRentabilidade.as_view(), name='list_rentabilidade'),
path('create', CreateRentabilidade.as_view(), name='create_rentabilidade'),
path('update/<int:pk>', UpdateRentabilidade.as_view(), name='update_rentabilidade'),

    ]

