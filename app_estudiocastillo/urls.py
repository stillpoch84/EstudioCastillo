from django.contrib import admin
from django.urls import path

   
from app_estudiocastillo.views import ClienteListView, ClienteCreateView


urlpatterns = [
    path('clientes/', ClienteListView.as_view(), name='lista_clientes'),
    path('crear-cliente/', ClienteCreateView.as_view(), name='crear_cliente'),
   
    
]