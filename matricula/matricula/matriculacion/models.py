from __future__ import unicode_literals

from django.db import models

class Inscribir(models.Model):
	cedula=models.CharField(max_length=10)
	nombres=models.CharField(max_length=30)
	apellidos=models.CharField(max_length=30)
	email=models.EmailField()
	def __str__(self):
		return self.cedula

