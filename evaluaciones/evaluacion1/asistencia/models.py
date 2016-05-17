from __future__ import unicode_literals

from django.db import models

class Docente(models.Model):
	nombres=models.CharField(max_length=30)
	apellidos=models.CharField(max_length=30)
	cedula=models.CharField(max_length=30)
	def __str__(self):
		return self.nombres
	def __str__(self):
		return self.apellidos
	def __str__(self):
		return self.cedula

class Asignatura(models.Model):
	nombre=models.CharField(max_length=30)
	credito=models.CharField(max_length=30)
	siglas=models.CharField(max_length=10)
	def __str__(self):
		return self.nombre
	def __str__(self):
		return self.credito
	def __str__(self):
		return self.siglas

