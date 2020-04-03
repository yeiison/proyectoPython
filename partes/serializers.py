from rest_framework import routers, serializers, viewsets
from .models import Parte

class ParteSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parte
        fields = ['id', 'fecha', 'tipo', 'marca', 'caracteristicas', 'cantidad', 'compra']
        pass