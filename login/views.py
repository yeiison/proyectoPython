from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .models import Login
from .serializers import LoginSerializers
from .serializers import AutenticarSerializers
from rest_framework import generics

# Create your views here.

class LoginsView (viewsets.ModelViewSet):
    queryset = Login.objects.all()          
    serializer_class = LoginSerializers 

#class LoginsView(generics.ListAPIView):
#    queryset = Login.objects.all()          
#    serializer_class = LoginSerializers    


class Password (generics.ListAPIView):

    queryset = Login.objects.all()          
    serializer_class = AutenticarSerializers

    def post (self, request, format=None):    

        usuario =  request.data['userName']         
        password = request.data['password']          
        print('userName',usuario)                     
        print('Password',password) 
        try:
            usuarioBD = usuario.objects.get(userName=usuario)
            if usuarioBD.password == password:
              return Response('usuario vallido', status=200)
        except usuario.DoesNotExist:
                pass
        return Response("Usuariono no valido", status = 500)
    
          

