from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class Entree(models.Model):
	name = models.CharField(max_length=50)	
	calories = models.PositiveSmallIntegerField()
	calories_from_fat = models.PositiveSmallIntegerField()
	total_fat = models.FloatField()
	saturated_fat = models.FloatField()
	trans_fat = models.FloatField()
	cholesterol = models.PositiveSmallIntegerField()
	sodium = models.PositiveSmallIntegerField()
	carbohydrates = models.PositiveSmallIntegerField()
	fiber = models.PositiveSmallIntegerField()
	sugar = models.PositiveSmallIntegerField()
	protein = models.PositiveSmallIntegerField()
	category = models.CharField(max_length=8)
	restaurant = models.CharField(max_length=10)


class UserInfo(models.Model):
	
	age = models.PositiveSmallIntegerField()
	sex = models.CharField(max_length=1)
	weight = models.PositiveSmallIntegerField()
	height = models.PositiveSmallIntegerField()
	macro_information = models.ForeignKey(Entree ,on_delete=models.PROTECT)	

