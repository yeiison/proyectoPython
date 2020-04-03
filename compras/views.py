from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .models import Compra
from .serializers import CompraSerializers

# Create your views here.
class ComprasView (viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializers