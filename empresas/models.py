from django.db import models

# Create your models here.
class Empresa (models.Model):
    nomCiudad = models.CharField(max_length=20)
    nomSucursal = models.CharField(max_length=20)
    