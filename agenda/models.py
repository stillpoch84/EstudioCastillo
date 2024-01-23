from django.db import models
from django import forms
from ckeditor.fields import RichTextField
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator


class Vencimiento(models.Model):
    impuesto = models.CharField(max_length=64, blank=False, null=False)
    fecha_vencimiento = models.DateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Ensure fecha_vencimiento is set
        if not self.fecha_vencimiento:
            # Set the day to the first day of the month
            self.fecha_vencimiento = self.fecha_vencimiento.replace(day=1)
        
        super().save(*args, **kwargs)
    


    def __str__(self):
        return f'{self.impuesto} | {self.fecha_vencimiento}'
