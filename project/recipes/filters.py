from django.contrib.auth.models import User
from recipes.models import Entree
import django_filters
from django import forms



class UserFilter(django_filters.FilterSet):
	class Meta:
		model = User
		fields = ['username' ]




class EntreeFilterCalories(django_filters.FilterSet):
	calories =  django_filters.NumberFilter(lookup_expr='lte')
	total_fat =  django_filters.NumberFilter(lookup_expr='lte')
	protein =  django_filters.NumberFilter(lookup_expr='gte')
	restaurant =  django_filters.CharFilter(lookup_expr='icontains')
	carbohydrates = django_filters.NumberFilter(lookup_expr='lte')
	
	class Meta:
		model = Entree
		fields = ['calories', 'restaurant', 'protein', 'carbohydrates', 'total_fat']