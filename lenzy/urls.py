"""lenzy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,re_path,include
from main.views import Userdetail,Airtex,Mootors,Autoparts,Carter,Opticat,Standard,BWD,Alllist,WVVE

urlpatterns = [
    path('admin/', admin.site.urls),
    path('airtex/', Airtex.as_view()),

    path('check/',Userdetail.as_view()),
    path('usmotors/',Mootors.as_view()),
    path('autoparts/', Autoparts.as_view()),
    path('carter/', Carter.as_view()),
    path('opticat/', Opticat.as_view()),
    path('standard/', Standard.as_view()),
    path('bwd/', BWD.as_view()),
    path('listall/', Alllist.as_view()),
    path('wvebrand/', BWD.as_view()),

    path('celery-progress/', include('celery_progress.urls')),
]
