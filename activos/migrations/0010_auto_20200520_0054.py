# Generated by Django 3.0.6 on 2020-05-20 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_correo'),
        ('compras', '0004_auto_20200520_0015'),
        ('activos', '0009_remove_activo_cantidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activo',
            name='caracteristicas',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='activos.Caracteristica'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activo',
            name='compra',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='compras.Compra'),
        ),
        migrations.AlterField(
            model_name='activo',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.User'),
        ),
    ]