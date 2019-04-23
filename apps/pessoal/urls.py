from django.urls import path

from .views import CreateFamilia, CreateMembro

urlpatterns = [

    path('', CreateFamilia.as_view(), name = 'create_famila'),
    path('', CreateMembro.as_view(), name = 'create_membro'),

]