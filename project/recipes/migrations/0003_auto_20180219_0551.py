# Generated by Django 2.0.2 on 2018-02-19 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20180219_0546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entree',
            name='saturated_fat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='entree',
            name='total_fat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='entree',
            name='trans_fat',
            field=models.FloatField(),
        ),
    ]
