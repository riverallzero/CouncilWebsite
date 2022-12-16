"""SED_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from qna import views

app_name = 'SED_prj'

urlpatterns = [
    # path('', include('single_pages.urls')),
    path('todo/', include('todo_app.urls')),
    path('smartfarm/', include('smartfarm.urls')),
    path('council/', include('council.urls')),
    path('location/', include('location.urls')),
    path('notice/', include('notice.urls')),
    path('partnership/', include('partnership.urls')),
    path('qna/', include('qna.urls')),
    path('room/', include('room.urls')),
    path('survey/', include('survey.urls')),
    path('admin/', admin.site.urls),
    path('common/', include('common.urls')),
    path('scheduler/', include('scheduler.urls')),
    path('', include('smartfarm.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)