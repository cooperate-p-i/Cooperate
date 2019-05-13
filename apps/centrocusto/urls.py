from django.urls import path

from .views import CreateCentroCusto, UpdateCentroCusto,DeleteCentroCusto,ListCentroDeCustos

urlpatterns = [

    path('novo', CreateCentroCusto.as_view(), name = 'create_centrocusto'),
    path('list', ListCentroDeCustos.as_view(), name = 'list_centrocusto'),
    path('delete/<int:pk>', DeleteCentroCusto.as_view(), name = 'delete_centrocusto'),
    path('update/<int:pk>', UpdateCentroCusto.as_view(), name = 'update_centrocusto'),


]