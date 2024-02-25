from django.urls import path, include
from django.contrib import admin
from blog import views
urlpatterns = [
path('', views.index, name='blog'),
]