from django.db import models

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
    areaTotal = models.DecimalField(max_digits=5, decimal_places=1)
    responsalvel = models.ForeignKey(Membro, on_delete=models.PROTECT)
    proprietario = models.ForeignKey(Familia, on_delete=models.PROTECT)
    areaReserva = models.DecimalField(max_digits=5, decimal_places=5, null=True, blank=True)
    culturaPrimaria = models.ManyToManyField(Cultura)
    rebanho1 = models.ManyToManyField(Rebanho)

    def __str__(self):
        return self.nome