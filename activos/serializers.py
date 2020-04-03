from rest_framework import routers, serializers, viewsets
from .models import Activo, Caracteristica

class CaracteristicaSerializers (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Caracteristica
        fields = ['id', 'procesador', 'generacion', 'ram', 'discoDuro', 'estadoDD']
        pass

class AtivoSerializers (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activo
        fields = ['id', 'fecha', 'cantidad', 'tipo', 'marca', 'referencia', 'estado', 'serial','valor', 'placa', 'codigo', 'caracteristicas', 'compra', 'empresa', 'user', 'parte' ]
        pass