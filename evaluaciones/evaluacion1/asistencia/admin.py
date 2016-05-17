from django.contrib import admin
from .models import Docente
from .models import Asignatura


class AdministrarDocente(admin.ModelAdmin):
	list_display = ["__str__","nombres","apellidos","cedula"]
	class Meta:
		model = Docente
admin.site.register(Docente,AdministrarDocente)

class AdministrarAsignatura(admin.ModelAdmin):
	list_display = ["__str__","nombre","credito","siglas"]
	class Meta2:
		model = Asignatura
admin.site.register(Asignatura,AdministrarAsignatura)