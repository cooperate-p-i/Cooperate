from django.db import models
from django.urls import reverse

from apps.pessoal.models import Membro, Familia

class Propriedade(models.Model):

    nome = models.CharField(max_length=(100))
    areaTotal = models.DecimalField(max_digits=10, decimal_places=1)
    responsavel = models.ForeignKey(Membro, on_delete=models.CASCADE)
    proprietario = models.ForeignKey(Familia, on_delete=models.CASCADE)
    areaReserva = models.DecimalField( max_digits=10, decimal_places=1, null=True, blank=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('detalhes_propriedade', args=[self.id])

class Cultura(models.Model):
    nome = models.CharField(max_length=(50))
    tipo = models.CharField(max_length=(20))
    areaPlantada = models.DecimalField(max_digits=5, decimal_places=2)
    propriedade = models.ManyToManyField(Propriedade, null=True, blank=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('list_cultura')

class Rebanho(models.Model):
    tipo = models.CharField(max_length=(30))
    quantidade = models.IntegerField
    propriedade = models.ManyToManyField(Propriedade, null=True, blank=True)