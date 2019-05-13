from django.db import models
from django.urls import reverse, reverse_lazy

from apps.cooperativa.models import Cooperativa
from apps.pessoal.models import Familia
from apps.centrocusto.models import Centrocusto

class ContasPagar(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=255)
    parcela_atual= models.CharField(max_length=30,null=True, blank=True)
    data_documento = models.DateField()
    data_pagar = models.DateField()
    cooperativa = models.ForeignKey(Cooperativa, on_delete=models.CASCADE)
    centrocusto = models.ForeignKey(Centrocusto, on_delete=models.CASCADE)
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    numero_parcela = models.IntegerField()
    numero_parcela_total = models.IntegerField(null=True, blank=True)
    status = models.NullBooleanField()



    def __str__(self):
            return self.nome

    def get_absolute_url(self):
        return reverse('select')