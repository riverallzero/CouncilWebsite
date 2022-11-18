from django.urls import path
from . import views

urlpatterns = [
    path('', views.notice),
    path('<int:pk>/', views.NoticeDetail.as_view()),
]