from datetime import date

from django.db import models


class Membro(models.Model):

    nome = models.CharField(max(100))
    cpf = models.BigIntegerField()
    rg = models.BigIntegerField()
    dataDeNascimento = models.DateField(auto_now=False, auto_now_add=False)


class Familia(models.Model):

    nome = models.CharField(max(100))
    dataDeCadastro = models.DateField(auto_now_add=False, auto_now=False, default=date.today())
    administrador = models.ForeignKey(Membro, on_delete=models.PROTECT)




