from django.db import models
from django.urls import reverse
from apps.ambiental.models import Producao


class Orcamento(models.Model):
    producao = models.ForeignKey(Producao, on_delete=models.PROTECT)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def get_absolute_url(self):
        return reverse('list_orcamento')

class Rentabilidade(models.Model):
    producao = models.ForeignKey(Producao, on_delete=models.PROTECT)
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def get_absolute_url(self):
        return reverse('list_orcamento')