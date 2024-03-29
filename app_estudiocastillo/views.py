from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django import forms

from app_estudiocastillo.models import Cliente


class ClienteListView(ListView):
    model = Cliente
    template_name = 'app_estudiocastillo/cliente_list.html'

    def get_queryset(self):
        # Get the ordering parameter from the URL, defaulting to 'razon_social'
        order_by = self.request.GET.get('order_by', 'razon_social')
        return Cliente.objects.all().order_by(order_by)
    
class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ('razon_social', 'CUIT', 'domicilio', 'localidad', 'provincia', 'contacto_nombre', 'celular', 'mail', 'forma', 'situacion_iva', 'ingresos_brutos', 'honorarios', 'recibe_factura')
    success_url = reverse_lazy('cliente_list')   

class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Cliente
    success_url = reverse_lazy('cliente_list')

class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ('razon_social', 'CUIT', 'domicilio', 'localidad', 'provincia', 'contacto_nombre', 'celular', 'mail', 'forma', 'situacion_iva', 'ingresos_brutos', 'honorarios', 'recibe_factura')
    success_url = reverse_lazy('cliente_list')

class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy('cliente_list')

class BuscarClienteView(ListView):
    model = Cliente
    template_name = 'app_estudiocastillo/cliente_search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Cliente.objects.filter(Q(razon_social__icontains=query)|Q(CUIT__icontains=query)|Q(contacto_nombre__icontains=query)|Q(forma__icontains=query)|Q(situacion_iva__icontains=query)|Q(ingresos_brutos__icontains=query)|Q(honorarios__icontains=query))
        return object_list

class HonorarioListView(ListView):
    model = Cliente
    template_name = 'app_estudiocastillo/honorario_list.html'
