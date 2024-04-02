from django.urls import path

from bulletin import views

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", views.home, name="home"),

]
