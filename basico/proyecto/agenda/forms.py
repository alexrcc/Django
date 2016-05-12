from django import forms

class Formulario(forms.Form):
	nombres=forms.CharField(max_length=30)
	apellidos=forms.CharField(max_length=30)
	correo=forms.Email()
	edad=forms.IntegerField()
