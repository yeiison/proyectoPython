# Generated by Django 3.0.4 on 2020-04-02 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='nomEmpresa',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
    ]
