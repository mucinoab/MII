"""MII URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from inicio.views import home_view
from resumenes.views import res_view
from newton.views import newton_view

from django.views.generic.base import RedirectView


favicon_view = RedirectView.as_view(url='/staticfiles/favicon.ico', permanent=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view, name='home'),
    path('', home_view, name='home'),
    path('resumenes/', res_view, name='resumenes'),
    path('favicon.ico', favicon_view),
    path('metodo_newton', newton_view)
]