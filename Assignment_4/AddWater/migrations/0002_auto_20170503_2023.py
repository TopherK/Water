# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-04 03:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AddWater', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='ProductCategory',
            field=models.CharField(choices=[('Sprk', 'Sparkling'), ('Flat', 'Flat')], max_length=4),
        ),
    ]
