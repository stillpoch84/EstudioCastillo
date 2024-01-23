from django.contrib import admin
from django.urls import path

   
from agenda.views import VencimientoListView, VencimientoCreateView, BuscarVencimientoView, VencimientoDetailView, VencimientoUpdateView, VencimientoDeleteView


urlpatterns = [
    path('vencimientos/', VencimientoListView.as_view(), name='vencimiento_list'),
    path('crear-vencimiento/', VencimientoCreateView.as_view(), name='vencimiento_create'),
    path('buscar-vencimiento/', BuscarVencimientoView.as_view(), name='vencimiento_search'),
    path('vencimiento/<int:pk>/', VencimientoDetailView.as_view(), name='ver_vencimiento'),
    path('editar-vencimiento/<int:pk>/', VencimientoUpdateView.as_view(), name="vencimiento_edit"),
    path('eliminar-vencimiento/<int:pk>/', VencimientoDeleteView.as_view(), name="vencimiento_delete"), 

     
    
]