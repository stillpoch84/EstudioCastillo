# forms.py
from django import forms
from .models import Vencimiento

class VencimientoForm(forms.ModelForm):
    class Meta:
        model = Vencimiento
        fields = ['impuesto', 'fecha_vencimiento']
