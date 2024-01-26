from django.db import models

class Vencimiento(models.Model):
 
    impuesto = models.CharField(max_length=100)
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return f'{self.impuesto} - Fecha de vencimientos: {self.fecha_vencimiento}'
    
class Impuestos(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name


