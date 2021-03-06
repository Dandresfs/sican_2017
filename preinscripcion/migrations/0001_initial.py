# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-01 21:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('radicados', '0003_radicado_municipio'),
        ('municipios', '0001_initial'),
        ('departamentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocentesPreinscritos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.BigIntegerField(unique=True)),
                ('primer_apellido', models.CharField(max_length=100)),
                ('segundo_apellido', models.CharField(blank=True, max_length=100)),
                ('primer_nombre', models.CharField(max_length=100)),
                ('segundo_nombre', models.CharField(blank=True, max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('correo', models.EmailField(blank=True, max_length=100, null=True)),
                ('telefono_fijo', models.BigIntegerField(blank=True, null=True)),
                ('telefono_celular', models.BigIntegerField(blank=True, null=True)),
                ('verificado', models.BooleanField(default=False)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamentos.Departamento')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='municipios.Municipio')),
                ('radicado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radicados.Radicado')),
            ],
            options={
                'ordering': ['primer_apellido'],
            },
        ),
    ]
