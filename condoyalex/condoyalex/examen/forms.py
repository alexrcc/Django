from django import forms
from .models import Compra

class FormularioCompra(forms.ModelForm):
	class Meta:
		model=Compra
		fields =["cant"]