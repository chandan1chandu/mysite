from django.conf.urls import url, include
#from django.urls import path
from django.conf.urls import url
from django.shortcuts import render
from django.views.generic import TemplateView

from . import views

urlpatterns = [
   url(r'^$', views.HomePageView.as_view()),
   url(r'^disp/$', views.AboutdisplayView.as_view()), 

]


