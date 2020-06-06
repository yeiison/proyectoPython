from django.db import models

from compras.models import Compra
from empresas.models import Empresa
from users.models import User
from partes.models import Parte
# Create your models here.
class Caracteristica (models.Model): 
    procesador = models.CharField(max_length=20)
    generacion = models.IntegerField()
    ram = models.IntegerField()
    discoDuro = models.IntegerField()
    estadoDD = models.CharField(max_length=20)

    def __str__ (self):     #Muestro los dombres de los objetos
        return self.procesador.__str__()

class Activo (models.Model):
    fecha = models.DateField()
    tipo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    referencia = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    serial = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=10, decimal_places=0)
    placa = models.CharField(max_length=20)
    codigo = models.IntegerField()

    #Relation one to many
    compra = models.ForeignKey(to=Compra, on_delete=models.CASCADE, null=True, blank=True) #preguntar si no quiero que se eliminin los registros en cascada si no solo los registros de esa clase
    empresa = models.ForeignKey(to=Empresa, on_delete=models.CASCADE, null=False, blank=False)
    caracteristicas = models.ForeignKey(to=Caracteristica, on_delete=models.CASCADE, null=False, blank=False) 
    #Relation one to one
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, null=True, blank=True)

    parte = models.OneToOneField(to=Parte, on_delete=models.CASCADE, null=True) 
    
