from django.db import models

class Vencimiento(models.Model):
    AUTONOMO = 'Autónomo'
    CARGAS_SOCIALES = 'Cargas Sociales'

    impuestos_lista = [
        (AUTONOMO, 'Autónomo'),
        (CARGAS_SOCIALES, 'Cargas Sociales'),
    ]

    impuesto = models.CharField(max_length=30, choices=impuestos_lista, blank=False, null=False)
    fecha_vencimiento = models.DateField(blank=False, null=False)

    def save(self, *args, **kwargs):
        # Ensure either autonomo or cargas_sociales has a value if fecha_vencimiento is set
        if self.fecha_vencimiento and not self.impuesto:
            raise ValueError("If fecha_vencimiento is set, tax_type must have a value.")
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.impuesto} | {self.fecha_vencimiento}'

