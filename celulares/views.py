from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .serializers import CelularSerializer
from .models import Celular

# Create your views here.
class CelularesView (viewsets.ModelViewSet):
    queryset = Celular.objects.all()
    serializer_class = CelularSerializer
