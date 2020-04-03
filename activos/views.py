from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .models import Activo, Caracteristica
from .serializers import AtivoSerializers, CaracteristicaSerializers

# Create your views here.
class CaracteristicasView (viewsets.ModelViewSet):
    queryset = Caracteristica.objects.all()
    serializer_class = CaracteristicaSerializers


class ActivosView (viewsets.ModelViewSet):
    queryset = Activo.objects.all()
    serializer_class = AtivoSerializers
    