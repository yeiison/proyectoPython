from rest_framework import routers, serializers, viewsets
from .models import Celular

class CelularSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Celular
        fields = ['id', 'marca', 'refernecia', 'serial', 'imei', 'email', 'numero', 'compra', 'empresa', 'users'] 
        pass