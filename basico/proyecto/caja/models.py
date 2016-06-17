from __future__ import unicode_literals

from django.db import models

class CajaAhorros(models.Model):
	nombre=models.CharField(max_length=30)
	siglas=models.CharField(max_length=5)
	logo=models.FilePathField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.nombre

class Cliente(models.Model):
	listaGenero= (('f','femenino'),('m','masculino'))
	listaEstado=(('soltero','soltero'),('casado','casado'),('divorciado','divorciado'),('viudo','viudo'))
	idCA=models.ForeignKey(CajaAhorros,on_delete=models.CASCADE,default="")
	nombres=models.CharField(max_length=30)
	apellidos=models.CharField(max_length=30)
	cedula=models.CharField(max_length=10, unique=True)
	correo=models.EmailField(max_length=30,blank=True,null=True)
	telefono=models.CharField(max_length=15,blank=True,null=True)
	celular=models.CharField(max_length=15,blank=True,null=True)
	direccion=models.TextField(max_length=100, default="direccion")
	sexo=models.CharField(max_length=10, choices=listaGenero)
	estadoCivil= models.CharField(max_length=10, choices=listaEstado)
	fechaNacimiento = models.DateField(blank=True, null=True)

	def __str__(self):
		return self.cedula

class CuentaAhorros(models.Model):
	idC=models.ForeignKey(Cliente, on_delete=models.CASCADE, default="")
	numeroCuenta= models.CharField(max_length=15)
	estado=models.BooleanField()
	fechaApertura= models.DateTimeField(auto_now=True, auto_now_add=False)
	saldo=models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return self.numeroCuenta

class Transaccion(models.Model):
	listaTransaccion = (('d','deposito'),('r','retiro'))
	idCuenta = models.ForeignKey(CuentaAhorros, on_delete=models.CASCADE, default="")
	fecha = models.DateTimeField(auto_now=True, auto_now_add=False)
	descripcion = models.TextField(max_length=50, default="dexcripcion")
	tipo = models.CharField(max_length=30, choices=listaTransaccion)
	valor = models.DecimalField(max_digits=5, decimal_places=2, default=0)

	def __str__(self):
		return self.idCuenta
