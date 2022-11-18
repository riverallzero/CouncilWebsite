from django.urls import path
from . import views

urlpatterns = [
    path('', views.survey),
    path('<int:pk>/', views.SurveyDetail.as_view()),
]