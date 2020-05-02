from django.db import models

# Create your models here.
class Empresa (models.Model):
    
    nomSucursal = models.CharField(max_length=20)
    nomCiudad = models.CharField(max_length=20)
    
    def __str__ (self):
        return self.nomCiudad.__str__() #PREGUNTAR POR QUEN NO APARECE EL NOMBRE
        #return self.nomCiudad.__str__()

    