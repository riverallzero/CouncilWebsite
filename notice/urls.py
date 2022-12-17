from django.urls import path
from . import views

app_name = 'notice'

urlpatterns = [
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('create_post/', views.PostCreate.as_view()),
    path('', views.index, name='index'),
    path('<int:pk>/', views.PostDetail.as_view(), name='detail'),
    path('notice/delete/<int:pk>/', views.post_delete, name='delete'),
]