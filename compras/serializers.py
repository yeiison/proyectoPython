from rest_framework import routers, serializers, viewsets
from .models import Compra

class CompraSerializers (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Compra
        fields = ['id', 'tipo', 'ordenCompra', 'estado']
        pass

