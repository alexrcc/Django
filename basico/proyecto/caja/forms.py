from django import forms
from .models import CajaAhorros

class Formulario(forms.Form):
	nombre=forms.CharField(max_length=30)
	siglas=forms.CharField(max_length=5)
	logo=forms.CharField(max_length=20)
	