from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions




from recipes.models import Recipe, Vote
from recipes.serializers import (
	RecipeSerializer, VoteSerializer
)

class RecipeListView(generics.ListCreateAPIView):
	queryset = Recipe.objects.all()
	serializer_class = RecipeSerializer

	def perform_create(self, serializer):
		serializer.save()

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Recipe.objects.all()
	serializer_class = RecipeSerializer


class VoteView(generics.ListCreateAPIView):
	queryset = Vote.objects.all()
	serializer_class = VoteSerializer


 # data makes the querydict unmuttable 
	# def get_serializer(self, *args, **kwargs):
	# 	"""
	# 	Return the serializer instance that should be used for validating and
	# 	deserializing input, and for serializing output.
	# 	"""
	# 	serializer_class = self.get_serializer_class()
	# 	kwargs['context'] = self.get_serializer_context()
	# 	if "data" in kwargs:
	# 		kwargs['data']['recipe'] = self.get_recipe().id
	# 	return serializer_class(*args, **kwargs)

	def get_recipe(self):
		pk = self.kwargs.get('pk')
		return get_object_or_404(Recipe, id=pk)

	def get_queryset(self):
		queryset = super().get_queryset()
		queryset = queryset.filter(recipes=self.get_recipe())
		return queryset

	def perform_create(self, serializer):
		recipe = self.get_recipe()
		serializer.save(content_object=recipe)



class VoteDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Vote.objects.all()
	serializer_class = VoteSerializer
	
	def get_recipe(self):
		pk = self.kwargs.get('pk')
		return get_object_or_404(Recipe, id=pk)

	def get_queryset(self):
		queryset = super().get_queryset()
		queryset = queryset.filter(recipes=self.get_recipe())
		return queryset

	def perform_create(self, serializer):
		target = self.get_recipe()
		defaults = serializer.data
		defaults.update(dict(target=target))
		obj, created = Vote.objects.update_or_create(
			recipes__id=target.id, 
			defaults=defaults
		)