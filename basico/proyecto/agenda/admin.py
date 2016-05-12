from django.contrib import admin
from .models import Contacto
from .models import Usuario
# Register your models here
class AdministrarContacto(admin.ModelAdmin):
	list_display = ["__str__","nombres","apellidos"]
	class Meta:
		model = Contacto
admin.site.register(Contacto,AdministrarContacto)

class AdministrarUsuario(admin.ModelAdmin):
	list_display = ["__str__","nombreUsuario"]
	class Meta2:
		model = Usuario
admin.site.register(Usuario,AdministrarUsuario)