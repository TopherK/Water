# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-12 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AddWater', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='ProductPHBalance',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14')]),
        ),
    ]
