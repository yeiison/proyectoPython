from django.db import models

# Create your models here.
class Celular (models.Model):
    fecha = models.DateField()
    marca = models.CharField(max_length=20)
    refernecia = models.CharField(max_length=20)
    serial = models.CharField(max_length=20)
    imei = models.IntegerField()
    email = models.EmailField()
    numero = models.IntegerField()