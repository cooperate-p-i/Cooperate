

from django.db import models
from django.utils.datetime_safe import date



class Familia(models.Model):

    nome = models.CharField(max_length=(100))

    dataDeCadastro = models.DateField(auto_now_add=False, auto_now=False, default=date.today)

    def __str__(self):
        return self.nome



class Membro(models.Model):

    nome = models.CharField(max_length=(100))
    cpf = models.BigIntegerField()
    rg = models.BigIntegerField()
    dataDeNascimento = models.DateField(auto_now=False, auto_now_add=False)
    familia = models.ForeignKey(Familia, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
