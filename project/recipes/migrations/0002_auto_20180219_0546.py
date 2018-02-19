# Generated by Django 2.0.2 on 2018-02-19 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entree',
            name='calories',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='entree',
            name='calories_from_fat',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='entree',
            name='carbohydrates',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='entree',
            name='cholesterol',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='entree',
            name='fiber',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='entree',
            name='protein',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='entree',
            name='saturated_fat',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='entree',
            name='sodium',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='entree',
            name='sugar',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='entree',
            name='total_fat',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='entree',
            name='trans_fat',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
