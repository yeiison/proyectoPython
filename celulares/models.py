from django.db import models

from compras.models import Compra
from empresas.models import Empresa
from users.models import User

# Create your models here.
class Celular (models.Model):
    fecha = models.DateField()
    marca = models.CharField(max_length=20)
    refernecia = models.CharField(max_length=20)
    serial = models.CharField(max_length=20)
    imei = models.IntegerField()
    email = models.EmailField()
    numero = models.IntegerField()

    #Relation one a many
    compra = models.ForeignKey(to=Compra, on_delete=models.CASCADE , null=True, blank=True)
    empresa = models.ForeignKey(to=Empresa, on_delete=models.CASCADE ,null=False, blank=False)

    #Relation one to one
    users = models.OneToOneField(to=User, on_delete=models.CASCADE, blank=True)