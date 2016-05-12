from __future__ import unicode_literals

from django.db import models

class Contacto(models.Model):
	nombres=models.CharField(max_length=30,blank=True)
	apellidos=models.CharField(max_length=30)
	cedula=models.CharField(max_length=30)
	email=models.EmailField()

#para python3 y todas sus versiones
	#def __str__(self):
	#	pass
#para python 2
	
	def __str__(self):
		return self.email
	def __str__(self):
		return self.nombres
	def __str__(self):
		return self.apellidos
	def __str__(self):
		return self.cedula

class Usuario(models.Model):
	nombreUsuario=models.CharField(max_length=30,blank=False)
	password=models.CharField(max_length=30)
def __str__(self):
	pass


