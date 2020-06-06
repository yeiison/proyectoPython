from rest_framework import routers, serializers, viewsets
from .models import Empresa
#hay varios tipos de serializadores
#Nos permiten definir al detalle cómo serán las respuestas que devolverá nuestro API y cómo procesaremos el contenido de las peticiones que nos lleguen.
class EmpresaSerializers (serializers.HyperlinkedModelSerializer): #https://www.django-rest-framework.org/#installation
    class Meta:
        model = Empresa
        fields =  ['id', 'nomEmpresa', 'nomCiudad', 'nomSubdivision']
        pass
