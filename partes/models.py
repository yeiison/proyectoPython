from django.db import models

# Create your models here.
class Parte (models.Model):
    fecha = models.DateField()
    tipo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    caracteristicas = models.CharField(max_length=30)
    cantidad = models.IntegerField()