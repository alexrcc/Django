from django.contrib import admin
from .models import Contacto
from .models import Usuario
# Register your models here
class AdministrarContacto(admin.ModelAdmin):
	list_display = ["__str__","nombres","apellidos","cedula"]
	list_editable = ["nombres","apellidos","cedula"]
	list_filter =["email","cedula","nombres"]
	search_fields=["nombres"]
	class Meta:
		model = Contacto
admin.site.register(Contacto,AdministrarContacto)

class AdministrarUsuario(admin.ModelAdmin):
	list_display = ["__str__","nombreUsuario"]
	class Meta2:
		model = Usuario
admin.site.register(Usuario,AdministrarUsuario)