from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

from django_pandas.managers import DataFrameManager


class Entree(models.Model):
	name = models.CharField(max_length=50)
	
	calories = models.DecimalField(max_digits=8, decimal_places=2)
	calories_from_fat = models.DecimalField(max_digits=5, decimal_places=2)
	total_fat = models.DecimalField(max_digits=5, decimal_places=2)
	saturated_fat = models.DecimalField(max_digits=5, decimal_places=2)
	trans_fat = models.DecimalField(max_digits=5, decimal_places=2)
	cholesterol = models.DecimalField(max_digits=5, decimal_places=2)
	sodium = models.DecimalField(max_digits=5, decimal_places=2)
	carbohydrates = models.DecimalField(max_digits=5, decimal_places=2)
	fiber = models.DecimalField(max_digits=5, decimal_places=2)
	sugar = models.DecimalField(max_digits=5, decimal_places=2)
	protein = models.DecimalField(max_digits=5, decimal_places=2)
	category = models.CharField(max_length=8)

	objects = DataFrameManager()


class UserInfo(models.Model):
	
	age = models.PositiveSmallIntegerField()
	sex = models.CharField(max_length=1)
	weight = models.PositiveSmallIntegerField()
	height = models.PositiveSmallIntegerField()
	macro_information = models.ForeignKey(Entree ,on_delete=models.PROTECT)	

	objects = DataFrameManager()
