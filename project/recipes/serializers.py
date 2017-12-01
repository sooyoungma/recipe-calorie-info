from rest_framework import serializers
from recipes.models import Recipe, Vote


class RecipeSerializer(serializers.ModelSerializer):

	create_vote = serializers.HyperlinkedIdentityField(view_name='recipes:votes')

	class Meta:
		model = Recipe
		fields = [ 'name', 'serving','calorie', 'create_vote', 'id' ]



class VoteSerializer(serializers.HyperlinkedModelSerializer):


	class Meta:
		model = Vote
		fields = ('url', 'activity_type', 'id')
		extra_kwargs = {
			"url": {"view_name": "recipes:recipe-detail"}
		}