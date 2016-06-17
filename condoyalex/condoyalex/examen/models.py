from __future__ import unicode_literals

from django.db import models

class Producto(models.Model):
	nombre=models.CharField(max_length=30)
	precio=models.DecimalField(max_digits=5, decimal_places=2)
	stock=models.IntegerField(default=0)

	def __str__(self):
		return self.nombre

class Compra(models.Model):
	idPro=models.ForeignKey(Producto,on_delete=models.CASCADE,default="")
	cant=models.IntegerField()
	def __str__(self):
		return self.cant
