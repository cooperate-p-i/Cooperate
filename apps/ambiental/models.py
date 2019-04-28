from django.db import models
from django.urls import reverse

from apps.pessoal.models import Membro, Familia


class Cultura(models.Model):
    nome = models.CharField(max_length=(50))
    tipo = models.CharField(max_length=(20))
    areaPlantada = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome


class Rebanho(models.Model):
    tipo = models.CharField(max_length=(30))
    quantidade = models.IntegerField

class Propriedade(models.Model):

    nome = models.CharField(max_length=(100))
    areaTotal = models.DecimalField(max_digits=10, decimal_places=1)
    responsavel = models.ForeignKey(Membro, on_delete=models.CASCADE)
    proprietario = models.ForeignKey(Familia, on_delete=models.CASCADE)
    areaReserva = models.DecimalField( max_digits=10, decimal_places=1, null=True, blank=True)
    culturaPrimaria = models.ManyToManyField(Cultura, null=True, blank=True)
    rebanho1 = models.ManyToManyField(Rebanho, null=True, blank=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('detalhes_propriedade', args=[self.id])