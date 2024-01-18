from django.contrib import admin
from django.urls import path

   
from app_estudiocastillo.views import ClienteListView, ClienteCreateView, BuscarClienteView, ClienteDetailView, ClienteUpdateView, ClienteDeleteView


urlpatterns = [
    path('clientes/', ClienteListView.as_view(), name='lista_clientes'),
    path('crear-cliente/', ClienteCreateView.as_view(), name='crear_cliente'),
    path('buscar-cliente/', BuscarClienteView.as_view(), name='buscar_cliente'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='ver_cliente'),
    path('editar-vino/<int:pk>/', ClienteUpdateView.as_view(), name="editar_cliente"),
    path('eliminar-vino/<int:pk>/', ClienteDeleteView.as_view(), name="eliminar_cliente"), 
   
    
]