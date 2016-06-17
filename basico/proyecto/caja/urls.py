from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', 'caja.views.listar'),
    url(r'^crear/$', 'caja.views.crear'),
    url(r'^modificar/$', 'caja.views.modificar'),
    url(r'^imprimir/$', 'caja.views.pdf'),
    url(r'^eliminar/$', 'caja.views.eliminar'),
    url(r'^login/$', 'caja.views.loguear'),
    url(r'^cuentas/$', 'caja.views.cuenta'),
    url(r'^cuentas/Gestion/$', 'caja.views.GestionEstado'),
    url(r'^cuentas/nueva/$', 'caja.views.NuevaCuenta'),
    
    ]