from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import url, include
import debug_toolbar

app_name = 'qna'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
]

if settings.DEBUG:
    urlpatterns += (
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )