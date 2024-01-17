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
    template_name = 'app_estudiocastillo/lista_clientes.html'
    
class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ('id', 'razon_social', 'CUIT', 'domicilio', 'localidad', 'provincia', 'contacto_nombre', 'celular', 'mail', 'forma', 'situacion_iva', 'ingresos_brutos')
    success_url = reverse_lazy('lista_clientes')   