# Generated by Django 3.0.4 on 2020-03-27 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=30)),
                ('lastNames', models.CharField(max_length=30)),
                ('costeCenter', models.CharField(max_length=10)),
            ],
        ),
    ]