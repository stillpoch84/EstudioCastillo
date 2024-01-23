from django.contrib import admin
from django.urls import path

   
from app_estudiocastillo.views import ClienteListView, ClienteCreateView, BuscarClienteView, ClienteDetailView, ClienteUpdateView, ClienteDeleteView


urlpatterns = [
    path('clientes/', ClienteListView.as_view(), name='cliente_list'),
    path('crear-cliente/', ClienteCreateView.as_view(), name='cliente_create'),
    path('buscar-cliente/', BuscarClienteView.as_view(), name='cliente_search'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='cliente_detail'),
    path('editar-cliente/<int:pk>/', ClienteUpdateView.as_view(), name="cliente_edit"),
    path('eliminar-cliente/<int:pk>/', ClienteDeleteView.as_view(), name="cliente_delete"), 
   
    
]