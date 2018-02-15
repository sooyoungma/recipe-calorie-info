"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.conf.urls import url, include
	2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from recipes import views

app_name = "recipes"

urlpatterns = [

	url(r'^recipes$', views.EntreeListView.as_view(), namespace="recipes"),
	url(r'^recipes/mcdonalds$', views.McdonaldsAPIView.as_view(), namespace="mcdonalds-nutrition"),
	url(r'^recipes/burgerking$', views.BurgerKingAPIView.as_view(), namespace="burgerking-nutrition"),
	url(r'^recipes/popeyes$', views.PopeyesAPIView.as_view(), namespace="popeyes-nutrition"),
	url(r'^recipes/wendys$', views.WendysAPIView.as_view(), namespace="wendys-nutrition"),

]

urlpatterns = format_suffix_patterns(urlpatterns)
