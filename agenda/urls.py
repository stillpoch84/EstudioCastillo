from django.contrib import admin
from django.urls import path

   
from agenda.views import ImpuestoListView, ImpuestoCreateView, BuscarImpuestoView, ImpuestoDetailView, ImpuestoUpdateView, ImpuestoDeleteView


urlpatterns = [
    path('impuestos/', ImpuestoListView.as_view(), name='impuesto_list'),
    path('crear-impuesto/', ImpuestoCreateView.as_view(), name='impuesto_create'),
    path('buscar-impuesto/', BuscarImpuestoView.as_view(), name='impuesto_search'),
    path('impuesto/<int:pk>/', ImpuestoDetailView.as_view(), name='ver_impuesto'),
    path('editar-impuesto/<int:pk>/', ImpuestoUpdateView.as_view(), name="impuesto_edit"),
    path('eliminar-impuesto/<int:pk>/', ImpuestoDeleteView.as_view(), name="impuesto_delete"), 

     
    
]