from django.db import models
from apps.pessoal.models import Familia



class Cultura(models.Model):
    nome = models.CharField(max(50))
    tipo = models.CharField(max(20))
    areaPlantada = models.DecimalField(max_digits=5, decimal_places=2)

class Rebanho(models.Model):
    tipo = models.CharField(max(30))
    quantidade = models.IntegerField




class Propriedade(models.Model):
    nome = models.charfield(max(100))
    areaTotal = models.DecimalField(max_digits=5, decimal_places=2)
    proprietario = models.ForeignKey(Familia, on_delete=models.PROTECT)
    areaReserva = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    culturaPrimaria = models.ForeignKey(Cultura, on_delete=models.PROTECT)
    culturaSecundaria = models.ForeignKey(Cultura, on_delete=models.PROTECT, null=True, blank=True)
    culturaTerciaria = models.ForeignKey(Cultura, on_delete=models.PROTECT, null=True, blank=True)
    rebanho1 = models.ForeignKey(Rebanho, on_delete=models.PROTECT, null=True, blank=True)
    rebanho2 = models.ForeignKey(Rebanho, on_delete=models.PROTECT, null=True, blank=True)
