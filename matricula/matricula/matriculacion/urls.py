from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', 'matriculacion.views.inicio'),
    url(r'^inscribir/$', 'matriculacion.views.inscribir'),
    url(r'^modificar/$', 'matriculacion.views.modificar'),
    ]