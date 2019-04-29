from django.contrib.auth.models import User
from django.db import models

class Cooperativa(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    cnpj = models.CharField(max_length=18, unique=True)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):

    nome = models.CharField(max_length=100)
    matricula = models.BigIntegerField(unique=True)
    cooperativa = models.ForeignKey(Cooperativa, on_delete=models.CASCADE)
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome