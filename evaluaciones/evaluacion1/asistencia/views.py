from django.shortcuts import render

from .models import Docente
from .forms import Formulario 


def inicio(request):
	f=Formulario(request.POST or None)
	context={
	"form":f,
	"titulo":"mi primer formulario"
	}
	if f.is_valid():
		f_data=f.cleaned_data
		n=f_data.get("nombres")
		a=f_data.get("apellidos")
		c=f_data.get("cedula")
		obj= Docente.objects.create(nombres=n,apellidos=a,cedula=c)

	return render(request,"inicio.html",context)

def presentacion(request):
	return render(request,"presentacion.html",{})
