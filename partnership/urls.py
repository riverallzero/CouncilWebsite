from django.urls import path
from . import views

urlpatterns = [
    path('', views.cafe),
    path('home', views.cafe, name='cafe'),
    path('convenience', views.convenience, name='convenience'),
    path('food', views.food, name='food'),
    path('bar', views.bar, name='bar'),
    path('index_cafe', views.index_cafe),
    path('index_convenience', views.index_convenience),
]