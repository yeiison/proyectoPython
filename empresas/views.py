from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .models import Empresa
from .serializers import EmpresaSerializers

# Create your views here.
#Al implementar ViewSet permite utilizar estas funcionalidades "GET, POST, HEAD, OPTIONS"
#Que funcionalidades se quieren con el API
class EmpresasView(viewsets.ModelViewSet):
    queryset = Empresa.objects.all() #Datos que quiero que se vean en el query
    serializer_class = EmpresaSerializers