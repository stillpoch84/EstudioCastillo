from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Cliente(models.Model):
    localidades_lista = [
        ('Adrogue', 'Adrogué'),
        ('Burzaco', 'Burzaco'),
        ('Longchamps', 'Longchamps'),
    ]

    provincias_lista = [
        ('Buenos Aires', 'Buenos Aires'),
        ('Mendoza', 'Mendoza'),
    ]

    forma_lista = [
        ('Cooperativa', 'Cooperativa'),
        ('Sociedad', 'Sociedad'),
        ('Unipersonal', 'Unipersonal'),
    ]

    situacioniva_lista = [
        ('Monotributo', 'Monotributo'),
        ('Inscripto', 'Inscripto'),
        ('Exento', 'Exento'),
    ]

    ingresosbrutos_lista = [
        ('Convenio', 'Convenio'),
        ('Local', 'Local'),
        ('Unificado', 'Unificado'),
    ]

    id = models.AutoField(primary_key=True)
    razon_social = models.CharField(max_length=128, blank=False, null=False)
    CUIT = models.CharField(max_length=11, blank=False, null=False)
    domicilio = models.CharField(max_length=128, blank=False, null=False)
    localidad = models.CharField(max_length=64, blank=False, null=False, choices=localidades_lista)
    provincia = models.CharField(max_length=64, blank=False, null=False, choices=provincias_lista)
    contacto_nombre = models.CharField(max_length=128, blank=False, null=False)
    celular = models.IntegerField(blank=False, null=False)
    mail = models.EmailField(blank=False, null=False)
    forma = models.CharField(max_length=64, blank=False, null=False, choices=forma_lista)
    situacion_iva = models.CharField(max_length=64, blank=False, null=False, choices=situacioniva_lista)
    ingresos_brutos = models.CharField(max_length=64, blank=False, null=False, choices=ingresosbrutos_lista)

    def __str__(self):
        return f'{self.razon_social} | {self.CUIT} | {self.domicilio} | {self.localidad} | {self.provincia} \
            | {self.contacto_nombre} | {self.celular} | {self.mail} | {self.forma} | {self.situacion_iva} | {self.ingresos_brutos}'
