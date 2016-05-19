from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', 'caja.views.listar'),
    url(r'^crear/$', 'caja.views.crear'),
    url(r'^modificar/$', 'caja.views.modificar'),
    ]