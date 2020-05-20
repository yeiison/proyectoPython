from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .models import Login
from .serializers import LoginSerializers


# Create your views here.
class LoginsView (viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializers