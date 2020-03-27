from django.db import models

# Create your models here.
class Compra(models.Model):
    tipo = models.CharField(max_length=20)
    ordenCompra = models.IntegerField(null=True)
    estado = models.CharField(max_length=20)


    