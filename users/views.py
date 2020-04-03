from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .models import User
from .serializers import UserSerializers


# Create your views here.
class UsersView (viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    