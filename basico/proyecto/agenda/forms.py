from django import forms
from .models import Contacto

class Formulario(forms.Form):
	cedula=forms.CharField(max_length=10)
	nombres=forms.CharField(max_length=30)
	apellidos=forms.CharField(max_length=30)
	correo=forms.EmailField()


class FormularioModeloA(forms.ModelForm):
	class Meta:
		model=Contacto
		fields =["nombres","apellidos","cedula","email"]
