# Generated by Django 3.0.4 on 2023-07-01 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ERPapp', '0002_auto_20230630_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ERPapp.Type'),
        ),
    ]