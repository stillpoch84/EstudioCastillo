from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator

# Create your models here.

class Cliente(models.Model):
    localidades_lista = [
        ('Adrogue', 'Adrogué'),
        ('Burzaco', 'Burzaco'),
        ('Longchamps', 'Longchamps'),
    ]

    provincias_lista = [
        ('Buenos Aires', 'Buenos Aires'),
        ('Catamarca', 'Catamarca'),
        ('Chaco', 'Chaco'),
        ('Chubut', 'Chubut'),
        ('Córdoba', 'Córdoba'),
        ('Corrientes', 'Corrientes'),
        ('Entre Ríos', 'Entre Ríos'),
        ('Formosa', 'Formosa'),
        ('Jujuy', 'Jujuy'),
        ('La Pampa', 'La Pampa'),
        ('La Rioja', 'La Rioja'),
        ('Mendoza', 'Mendoza'),
        ('Misiones', 'Misiones'),
        ('Neuquén', 'Neuquén'),
        ('Río Negro', 'Río Negro'),
        ('Salta', 'Salta'),
        ('San Juan', 'San Juan'),
        ('San Luis', 'San Luis'),
        ('Santa Cruz', 'Santa Cruz'),
        ('Santa Fe', 'Santa Fe'),
        ('Santiago del Estero', 'Santiago del Estero'),
        ('Tierra del Fuego', 'Tierra del Fuego'),
        ('Tucumán', 'Tucumán'),
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
    CUIT = models.CharField(max_length=11,
        blank=False,
        null=False,
        validators=[
            MinLengthValidator(limit_value=11, message="El CUITdebe tener 11 dígitos."),
            MaxLengthValidator(limit_value=11, message="El CUITdebe tener 11 dígitos."),
            RegexValidator(regex=r'^\d{11}$', message="El CUITdebe tener 11 dígitos.")
        ]
    )
    domicilio = models.CharField(max_length=128, blank=False, null=False)
    localidad = models.CharField(max_length=64, blank=False, null=False, choices=localidades_lista)
    provincia = models.CharField(max_length=64, blank=False, null=False, choices=provincias_lista)
    contacto_nombre = models.CharField(max_length=128, blank=False, null=False)
    celular = models.CharField(
        max_length=10,
        blank=False,
        null=False,
        validators=[
            MaxLengthValidator(limit_value=10, message="El número de celular debe tener 10 dígitos."),
            MinLengthValidator(limit_value=10, message="El número de celular debe tener 10 dígitos."),
            RegexValidator(regex=r'^\d{10}$', message="El número de celular debe tener 10 dígitos.")
        ]
    )
    mail = models.EmailField(blank=False, null=False)
    forma = models.CharField(max_length=64, blank=False, null=False, choices=forma_lista)
    situacion_iva = models.CharField(max_length=64, blank=False, null=False, choices=situacioniva_lista)
    ingresos_brutos = models.CharField(max_length=64, blank=False, null=False, choices=ingresosbrutos_lista)

    def __str__(self):
        return f'{self.razon_social} | {self.CUIT} | {self.domicilio} | {self.localidad} | {self.provincia} \
            | {self.contacto_nombre} | {self.celular} | {self.mail} | {self.forma} | {self.situacion_iva} | {self.ingresos_brutos}'
