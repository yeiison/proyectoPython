# Generated by Django 3.0.4 on 2020-03-27 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('cantidad', models.IntegerField()),
                ('tipo', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=20)),
                ('referencia', models.CharField(max_length=20)),
                ('estado', models.CharField(max_length=20)),
                ('serial', models.CharField(max_length=20)),
                ('valor', models.DecimalField(decimal_places=0, max_digits=10)),
                ('placa', models.CharField(max_length=20)),
                ('codigo', models.IntegerField()),
            ],
        ),
    ]
