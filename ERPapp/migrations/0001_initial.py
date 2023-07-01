# Generated by Django 3.0.4 on 2023-06-30 20:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=100, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=50, verbose_name='Apellido')),
                ('dni', models.CharField(max_length=20, unique=True, verbose_name='Documento de identificación')),
                ('date_joined', models.DateField(default=datetime.datetime(2023, 6, 30, 15, 49, 48, 83932), verbose_name='Fecha de registro')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('age', models.PositiveIntegerField(default=0)),
                ('salary', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('state', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='avatar/%Y/%m/%d')),
                ('cv', models.FileField(blank=True, null=True, upload_to='cv/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'empleado',
                'ordering': ['id'],
            },
        ),
    ]