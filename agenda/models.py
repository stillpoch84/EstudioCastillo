from django.db import models
from django import forms
from ckeditor.fields import RichTextField
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator


class Vencimiento(models.Model):
    impuesto = models.CharField(max_length=64, blank=False, null=False)
    fecha_vencimiento = models.DateField(blank=True, null=True)
    


    def __str__(self):
        return f'{self.impuesto} | {self.fecha_vencimiento}'
