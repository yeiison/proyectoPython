# Generated by Django 3.0.6 on 2020-05-20 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0008_activo_caracteristicas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activo',
            name='cantidad',
        ),
    ]
