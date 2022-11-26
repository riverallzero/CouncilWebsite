from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import url, include
import debug_toolbar

app_name = 'survey'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('create/', views.question_create, name='question_create'),
]

if settings.DEBUG:
    urlpatterns += (
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )