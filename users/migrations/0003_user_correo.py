# Generated by Django 3.0.6 on 2020-05-20 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='correo',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
