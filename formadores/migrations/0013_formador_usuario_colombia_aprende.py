# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-27 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formadores', '0012_auto_20160920_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='formador',
            name='usuario_colombia_aprende',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
