from django.db import models

# Create your models here.
class Empresa (models.Model):
    #nomEmpresa = models.CharField(max_length=20) PREGUNTAR COMO CREAR UNA NUEVA COLUMNA EN LA BD
    nomCiudad = models.CharField(max_length=20)
    nomSucursal = models.CharField(max_length=20)

    def str (self):
        return self.nomCiudad.__str__() #PREGUNTAR POR QUEN NO APARECE EL NOMBRE
        #return self.nomCiudad.__str__()

    