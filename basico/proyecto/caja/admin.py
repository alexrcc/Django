from django.contrib import admin
from .models import Cliente
from .models import CajaAhorros
# Register your models here.
class AdminCaja(admin.ModelAdmin):
	list_dislay =["__str__","nombre"]
	class Meta2:
		model = CajaAhorros
admin.site.register(CajaAhorros,AdminCaja)
class AdminCliente(admin.ModelAdmin):
	list_dislay =["__str__","nombres","apellidos","cedula"]
	class Meta:
		model = Cliente
admin.site.register(Cliente,AdminCliente)