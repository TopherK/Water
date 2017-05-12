# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-12 20:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Flavors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductFlavor', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(max_length=100, unique=True)),
                ('ProductCategory', models.CharField(choices=[('Sparkling', 'Sparkling'), ('Flat', 'Flat')], max_length=9)),
                ('ProductTotalScore', models.PositiveSmallIntegerField()),
                ('NumberofReviews', models.PositiveSmallIntegerField()),
                ('ProductTotalHydrationFactor', models.PositiveIntegerField(default=0)),
                ('ProductPHBalance', models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14')], default=7)),
                ('ProductFlavor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AddWater.Flavors')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ReviewScore', models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('HydrationFactor', models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1)),
                ('ReviewText', models.TextField()),
                ('ReviewDate', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('ProductName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AddWater.Products')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='ProductName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AddWater.Products'),
        ),
    ]
