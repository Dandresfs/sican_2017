# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-09-12 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vigencia2017', '0009_auto_20170829_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='corte',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='Cortes/Vigencia 2017/'),
        ),
    ]
