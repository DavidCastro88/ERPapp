# Generated by Django 3.0.4 on 2023-06-30 20:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ERPapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_joined',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de registro'),
        ),
    ]
