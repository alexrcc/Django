from django.contrib import admin
from .models import Producto
# Register your models here.
class AdminProducto(admin.ModelAdmin):
	list_dislay =["__str__","nombre","precio","stock"]
	class Meta:
		model = Producto
admin.site.register(Producto,AdminProducto)