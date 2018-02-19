from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions


from recipes.permissions import EntreeIsOwnerOrReadOnly


from recipes.models import Entree, UserInfo
from recipes.serializers import (
	EntreeSerializer, UserInfoSerializer
)
from rest_pandas import PandasSimpleView
import pandas as pd



class EntreeListView(generics.ListCreateAPIView):
	queryset = Entree.objects.all()
	serializer_class = EntreeSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

	def get_entree(self):
		pk = self.kwargs.get('pk')
		return get_object_or_404(Entree, id=pk)

class EntreeDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Entree.objects.all()
	serializer_class = EntreeSerializer

	permission_classes = (EntreeIsOwnerOrReadOnly,)




class UserListView(generics.ListCreateAPIView):
	queryset = UserInfo.objects.all()
	serializer_class = UserInfoSerializer


	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class UserInfoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = UserInfo.objects.all()
	serializer_class = UserInfoSerializer



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

	def get_queryset(self):
		queryset = super().get_queryset()
		queryset = queryset.filter(recipes=self.get_recipe())
		return queryset

	def perform_create(self, serializer):
		recipe = self.get_recipe()
		serializer.save(content_object=recipe)


