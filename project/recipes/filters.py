from django.contrib.auth.models import User
from recipes.models import Entree
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username' ]




class EntreeFilterCalories(django_filters.FilterSet):
	class Meta:
		model = Entree
		fields = { 'name' : ['iexact'],
		'calories' : ['lt'],
		'protein' : ['gt']
		}