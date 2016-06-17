from django import forms
from .models import CajaAhorros
from .models import Cliente, Transaccion



class Formulario(forms.Form):
	nombre=forms.CharField(max_length=30)
	siglas=forms.CharField(max_length=5)
	logo=forms.CharField(max_length=20)

class FormularioCliente(forms.ModelForm):
	class Meta:
		model=Cliente
		fields =["nombres","apellidos","cedula","correo","telefono","celular","direccion","sexo",
		"estadoCivil","fechaNacimiento"]

class FormularioClienteModificar(forms.ModelForm):
	class Meta:
		model=Cliente
		fields =["nombres","apellidos","correo","telefono","celular","direccion","sexo",
		"estadoCivil","fechaNacimiento"]
class FormularioTransaccion(forms.ModelForm):
	class Meta:
		model=Transaccion
		fields =["tipo","valor"]

