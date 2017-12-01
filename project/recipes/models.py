from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

class Vote(models.Model):
	LIKE = 'L'
	DISLIKE = 'D'
	ACTIVITY_TYPES = (
		(LIKE, 'Like'),
		(DISLIKE, 'Dislike'),
	)
	activity_type = models.CharField(max_length=1, choices=ACTIVITY_TYPES)

	# Below the mandatory fields for generic relation
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey()


class Recipe(models.Model):
	name = models.CharField(max_length=100)
	serving = models.DecimalField(max_digits=3, decimal_places=2)
	calorie = models.DecimalField(max_digits=8, decimal_places=2)

	vote = GenericRelation(
		Vote,
		related_query_name='recipes'

	)


