"""app_alumnos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from alumnos.views import alumnos_views, get_alumnos
from clases.views import clases_views, get_clases,get_clase

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alumnos/',alumnos_views),
    path('clases/',clases_views),
    path('get_clases/',get_clases),
    path('get_clase/<clase_id>/', get_clase),
    path('get_alumnos/',get_alumnos)
]
