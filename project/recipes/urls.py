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
from . import views

urlpatterns = [
    url(r'^recipes$', views.RecipeListView.as_view(), name="recipes"),
    url(r'^recipes/(?P<pk>[0-9]+)$', views.RecipeDetail.as_view(), name="recipe-detail"),
    url(r'^recipes/(?P<pk>[0-9]+)/vote$', views.VoteView.as_view(), name="votes"),
    url(r'^votes/(?P<pk>[0-9]+)$', views.VoteDetail.as_view(), name="vote-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)