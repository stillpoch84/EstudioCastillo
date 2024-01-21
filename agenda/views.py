from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django import forms

from agenda.models import Impuesto


class ImpuestoListView(ListView):
    model = Impuesto
    template_name = 'impuestos/impuesto_list.html'
    
class ImpuestoCreateView(LoginRequiredMixin, CreateView):
    model = Impuesto
    fields = ('impuesto', 'fecha_vencimiento')
    success_url = reverse_lazy('impuesto_list')  

class BuscarImpuestoView(ListView):
    model = Impuesto
    template_name = 'agenda/impuesto_search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Impuesto.objects.filter(Q(impuesto__icontains=query))
        return object_list
    
class ImpuestoDetailView(LoginRequiredMixin, DetailView):
    model = Impuesto
    success_url = reverse_lazy('impuesto_list')

class ImpuestoUpdateView(LoginRequiredMixin, UpdateView):
    model = Impuesto
    fields = ('impuesto', 'fecha_vencimiento')
    success_url = reverse_lazy('impuesto_list')

class ImpuestoDeleteView(LoginRequiredMixin, DeleteView):
    model = Impuesto
    success_url = reverse_lazy('impuesto_list')