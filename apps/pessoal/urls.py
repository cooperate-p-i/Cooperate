from django.urls import path

from .views import CreateFamilia, CreateMembro, ListMembro, ListFamilia, DeleteFamilia, UpdateFamilia

urlpatterns = [

    path('novo', CreateFamilia.as_view(), name = 'create_famila'),
    path('novo', CreateMembro.as_view(), name = 'create_membro'),
    path('', ListFamilia.as_view(), name = 'list_familia'),
    path('/list/<int:familia_id>', ListMembro.as_view(), name = 'list_membro'),
    path('/delete/<int:pk>', DeleteFamilia.as_view(), name = 'delete_familia'),
    path('update/<int:pk>', UpdateFamilia.as_view(), name = 'update_familia'),


]