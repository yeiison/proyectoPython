from django.db import models

# Create your models here.

class Activo (models.Model):
    fecha = models.DateField()
    cantidad = models.IntegerField()
    tipo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    referencia = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    serial = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=10, decimal_places=0)
    placa = models.CharField(max_length=20)
    codigo = models.IntegerField()

class Caracteristicas (models.Model):
    procesador = models.CharField(max_length=20)
    generacion = models.IntegerField()
    ram = models.IntegerField()
    discoDuro = models.IntegerField()
    estadoDD = models.CharField(max_length=20)
