from django.db import models

# Create your models here.
class Compra(models.Model):
    
    fecha = models.DateField()
    tipo = models.CharField(max_length=20)
    ordenCompra = models.IntegerField(null=True)
    estado = models.CharField(max_length=20)

    def __str__ (self):     #Muestro los dombres de los objetos
        return self.ordenCompra.__str__()


    