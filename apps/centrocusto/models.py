from django.db import models
class Centrocusto (models.Model):
    nome = models.CharField(max_length=(100), unique=True)
    descricao = models.TextField(max_length=(100), unique=True)


    def __str__(self):
            return self.nome