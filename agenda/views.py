from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django import forms

from agenda.models import Vencimiento


class VencimientoListView(ListView):
    model = Vencimiento
    template_name = 'vencimiento/vencimiento_list.html'
    
class VencimientoCreateView(LoginRequiredMixin, CreateView):
    model = Vencimiento
    fields = ('impuesto', 'fecha_vencimiento')
    success_url = reverse_lazy('vencimiento_list')  

class BuscarVencimientoView(ListView):
    model = Vencimiento
    template_name = 'agenda/vencimiento_search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Vencimiento.objects.filter(Q(impuesto__icontains=query))
        return object_list
    
class VencimientoDetailView(LoginRequiredMixin, DetailView):
    model = Vencimiento
    success_url = reverse_lazy('vencimiento_list')

class VencimientoUpdateView(LoginRequiredMixin, UpdateView):
    model = Vencimiento
    fields = ('impuesto', 'fecha_vencimiento')
    success_url = reverse_lazy('vencimiento_list')

class VencimientoDeleteView(LoginRequiredMixin, DeleteView):
    model = Vencimiento
    success_url = reverse_lazy('vencimiento_list')