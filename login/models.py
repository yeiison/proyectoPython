from django.db import models

# Create your models here.
class Login(models.Model):
    names = models.CharField(max_length=30)
    lastNames = models.CharField(max_length=30)
    userName = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__ (self):     #Muestro los dombres de los objetos
        return self.userName.__str__()