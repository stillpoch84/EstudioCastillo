from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django import forms

from agenda.models import Vencimiento
from .forms import VencimientoForm


class VencimientoListView(ListView):
    model = Vencimiento
    template_name = 'vencimiento/vencimiento_list.html'
    
class VencimientoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'agenda/vencimiento_create.html' 
    form_class = VencimientoForm
    success_url = reverse_lazy('vencimiento_list')

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        impuestos = Vencimiento.impuestos_lista
        form_kwargs['initial'] = {'impuesto': impuesto for impuesto, _ in impuestos}
        return form_kwargs

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['impuestos'] = Vencimiento.impuestos_lista
        return context  

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