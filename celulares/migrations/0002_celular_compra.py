# Generated by Django 3.0.4 on 2020-03-27 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0002_compra_ordencompra'),
        ('celulares', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='celular',
            name='compra',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='compras.Compra'),
            preserve_default=False,
        ),
    ]
