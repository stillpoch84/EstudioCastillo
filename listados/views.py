from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django import forms
from app_estudiocastillo.models import Cliente

class AutonomosListView(ListView):
    model = Cliente
    template_name = 'app_estudiocastillo/cliente_lista.html'