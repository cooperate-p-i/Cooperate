from django.contrib import admin

# Register your models here.
from apps.cooperativa.models import Cooperativa, Funcionario

admin.site.register(Cooperativa)
admin.site.register(Funcionario)