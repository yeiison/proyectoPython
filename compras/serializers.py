from rest_framework import routers, serializers, viewsets
from .models import Compra

class CompraSerializers (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Compra
        fields = ['id', 'fecha', 'tipo', 'ordenCompra', 'estado']
        pass

