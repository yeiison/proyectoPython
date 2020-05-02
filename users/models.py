from django.db import models

# Create your models here.
class User(models.Model):
    names = models.CharField(max_length=30)
    lastNames = models.CharField(max_length=30)
    document = models.IntegerField(null=True)
    costeCenter = models.CharField(max_length=10)

    def __str__ (self):     #Muestro los dombres de los objetos
        return self.names.__str__()
    