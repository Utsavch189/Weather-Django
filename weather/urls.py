from django.contrib import admin
from django.urls import path,include
from django.urls.resolvers import URLPattern
from weather import views
urlpatterns=[
path('',views.weather,name="weather"),

]