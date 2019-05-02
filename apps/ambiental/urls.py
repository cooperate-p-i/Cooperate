from django.urls import path

from apps.ambiental.views import CreatePropriedade, UpdatePropriedade, DetailPropriedade, ListPropriedade, homeAmbiental

urlpatterns =  [

    path('create/<int:familia_id>', CreatePropriedade.as_view(), name = 'create_propriedade'),
    path('update/<int:pk>', UpdatePropriedade.as_view(), name = 'update_propriedade'),
    path('detail/<int:pk>', DetailPropriedade.as_view(), name = 'detalhes_propriedade'),
    path('', ListPropriedade.as_view(), name = 'list_propriedade'),

    path('modulo', homeAmbiental, name = 'home_ambiental'),


]