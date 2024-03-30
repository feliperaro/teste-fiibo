from django.db import models

class DataEntry(models.Model):
    notas = models.CharField(max_length=255)
    competencia = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
