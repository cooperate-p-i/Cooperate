

from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils.datetime_safe import date




class Familia(models.Model):

    nome = models.CharField(max_length=(100), unique=True)

    dataDeCadastro = models.DateField(auto_now_add=False, auto_now=False, default=date.today)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse_lazy('list_familia')

class Membro(models.Model):

    nome = models.CharField(max_length=(100), unique=True)
    cpf = models.BigIntegerField(unique=True)
    rg = models.BigIntegerField(unique=True)
    dataDeNascimento = models.DateField(auto_now=False, auto_now_add=False)
    familia = models.ForeignKey(Familia, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse_lazy('list_familia')
