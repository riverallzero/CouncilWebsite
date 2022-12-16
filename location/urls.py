from django.urls import path
from . import views

urlpatterns = [
    path('', views.location),
    path('index', views.index),
]