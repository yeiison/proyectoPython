from rest_framework import routers, serializers, viewsets
from .models import User

class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'names', 'lastNames', 'document', 'costeCenter']
        pass