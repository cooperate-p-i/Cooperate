from django.urls import path

from apps.ambiental.views import CreatePropriedade, UpdatePropriedade, DetailPropriedade, ListPropriedade, homeAmbiental,\
                                   CreateCultura, ListCultura, UpdateCultura, ListProducao, UpdateProducao,CreateProducao




urlpatterns =  [

    path('create/<int:familia_id>', CreatePropriedade.as_view(), name = 'create_propriedade'),
    path('update/<int:pk>', UpdatePropriedade.as_view(), name = 'update_propriedade'),
    path('detail/<int:pk>', DetailPropriedade.as_view(), name = 'detalhes_propriedade'),
    path('', ListPropriedade.as_view(), name = 'list_propriedade'),

    path('modulo', homeAmbiental, name = 'home_ambiental'),

    path('create', CreateCultura.as_view(), name = 'create_cultura'),
    path('list', ListCultura.as_view(), name = 'list_cultura'),
    path('update/<int:pk>', UpdateCultura.as_view(), name = 'update_cultura'),

    path('listagem', ListProducao.as_view(), name = 'list_producao'),
    path('criar', CreateProducao.as_view(), name = 'create_producao'),
    path('update/<int:pk>', UpdateProducao.as_view(), name = 'update_producao'),



]