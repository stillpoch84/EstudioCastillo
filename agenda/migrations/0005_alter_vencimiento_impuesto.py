# Generated by Django 5.0.1 on 2024-01-26 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0004_alter_vencimiento_fecha_vencimiento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vencimiento',
            name='impuesto',
            field=models.CharField(max_length=100),
        ),
    ]
