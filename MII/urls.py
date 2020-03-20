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
import django
from django.conf.urls import url
from django.views.generic import TemplateView
from pkg_resources import parse_version
from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView

from error.views import errors_view
from inicio.views import home_view
from newton.views import newton_view, newton_calcula, newton_view_multi, newton_multi
from punto_fijo.views import fijo_view, fijo_calcula, fijo_ejemplo_1, fijo_ejemplo_2, fijo_ejemplo_3
from resumenes.views import res_view, metodos_views
from lagrange.views import lagrange_view
from cuad import views

django_version = parse_version(django.get_version())
if django_version <= parse_version("1.9"):
    from django.conf.urls import patterns

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('resumenes/', res_view),
    path('favicon.ico/', favicon_view),
    path('metodo_newton/', newton_view),
    path('metodo_newton/?f=<str:fun>&ini<str:in>/', newton_calcula),
    path('error/', errors_view),
    path('metodos/', metodos_views),
    path('punto_fijo/', fijo_view),
    path('punto_fijo_calcula/', fijo_calcula),
    path('fijo_ejemplo1/', fijo_ejemplo_1),
    path('fijo_ejemplo2/', fijo_ejemplo_2),
    path('fijo_ejemplo3/', fijo_ejemplo_3),
    path('newton_Multi/', newton_view_multi),
    path('newton_Multi_calcula/', newton_multi),
    path('lagrange_', lagrange_view),
    path('cuad/', views.HomeView.as_view()), 
    path('api', views.ChartData.as_view()),  
]
