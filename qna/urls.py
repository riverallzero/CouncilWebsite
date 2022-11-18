from django.urls import path
from . import views

urlpatterns = [
    path('', views.qna),
    path('<int:pk>/', views.QnaDetail.as_view()),
]