from django.db import models
from compras.models import Compra

# Create your models here.
class Parte (models.Model):
    fecha = models.DateField()
    tipo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    caracteristicas = models.CharField(max_length=30)
    cantidad = models.IntegerField()

    compra = models.ForeignKey(to=Compra, on_delete=models.CASCADE, null=True, blank=False)

    def __str__ (self):     #Muestro los Nombres de los objetos
        return self.tipo.__str__()