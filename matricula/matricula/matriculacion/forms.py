from django import forms
from .models import Inscribir
class Formulario(forms.Form):
	cedula=forms.CharField(max_length=10)
	nombres=forms.CharField(max_length=30)
	apellidos=forms.CharField(max_length=30)
	email=forms.EmailField()
class FormularioEditar(forms.ModelForm):
	class Meta:
		model=Inscribir
		fields =["nombres","apellidos","email"]