from django.db import models
from django.urls import reverse

from apps.cooperativa.models import Cooperativa


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)
    endereco = models.CharField(max_length=100)
    cooperativa = models.ForeignKey(Cooperativa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('list_cliente')