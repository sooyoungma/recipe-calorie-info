# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-20 04:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20180219_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entree',
            name='calories',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='entree',
            name='calories_from_fat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='entree',
            name='carbohydrates',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='entree',
            name='cholesterol',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='entree',
            name='fiber',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='entree',
            name='protein',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='entree',
            name='sodium',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='entree',
            name='sugar',
            field=models.FloatField(),
        ),
    ]
