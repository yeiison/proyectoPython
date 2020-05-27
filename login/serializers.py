from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Login

class LoginSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Login
        fields = ['id', 'names', 'lastNames', 'userName']
        pass
     