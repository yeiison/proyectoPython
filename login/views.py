from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .models import Login
from .serializers import LoginSerializers
from rest_framework import generics

# Create your views here.

class LoginsView(generics.ListAPIView):
    queryset = Login.objects.all()          
    serializer_class = LoginSerializers    

    def post (self, request, format=None):         
      usuario =  request.data['userName']         
      password = request.data['password']          
      print('Usuario',usuario)                    
      print('Password',password) 
                           
