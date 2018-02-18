from rest_framework import serializers
from recipes.models import Entree, UserInfo


class EntreeSerializer(serializers.ModelSerializer):


	class Meta:
		model = Entree
		fields = '__all__'


class UserInfoSerializer(serializers.ModelSerializer):

	class Meta:
		model = UserInfo
		fields = '__all__'