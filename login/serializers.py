from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Login

class LoginSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Login
        fields = ['id', 'names', 'lastNames', 'userName', 'password']
        pass
     
    def create (self, validate_data):
        instance = Login ()
        instance.names = validate_data.get('names')
        instance.lastNames = validate_data.get('lastNames')
        instance.userName = validate_data.get('userName')
        instance.set_ = validate_data.get('password')
        instance.save()
        return instance

    def validate_userName (self, data):
        logins = Login.objects.filter(lo)


