from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .models import Parte
from .serializers import ParteSerializers

# Create your views here.

class PartesView (viewsets.ModelViewSet):
    queryset = Parte.objects.all()
    serializer_class = ParteSerializers
