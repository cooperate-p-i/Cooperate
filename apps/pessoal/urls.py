from django.urls import path

from .views import CreateFamilia, CreateMembro, ListMembro, ListFamilia, DeleteFamilia, UpdateFamilia, DetailMembro, UpdateMembro

urlpatterns = [

    path('novo', CreateFamilia.as_view(), name = 'create_famila'),
    path('create/<int:familia_id>', CreateMembro.as_view(), name = 'create_membro'),
    path('', ListFamilia.as_view(), name = 'list_familia'),
    path('list/<int:familia_id>', ListMembro.as_view(), name = 'list_membro'),
    path('detail/<int:pk>', DetailMembro.as_view(), name = 'detalhes_membro'),
    path('delete/<int:pk>', DeleteFamilia.as_view(), name = 'delete_familia'),
    path('update/<int:pk>', UpdateFamilia.as_view(), name = 'update_familia'),
    path('atualiza/<int:pk>', UpdateMembro.as_view(), name = 'update_membro'),



]