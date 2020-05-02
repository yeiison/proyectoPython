"""deviceManage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets 
from empresas.views import EmpresasView
from activos.views import ActivosView, CaracteristicasView
from celulares.views import CelularesView
from compras.views import ComprasView
from partes.views import PartesView
from users.views import UsersView




# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'empresas', EmpresasView)
router.register(r'activos', ActivosView, CaracteristicasView)
router.register(r'caracteristicas', CaracteristicasView)
router.register(r'celulares', CelularesView)
router.register(r'compras', ComprasView)
router.register(r'partes', PartesView)
router.register(r'users', UsersView)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]