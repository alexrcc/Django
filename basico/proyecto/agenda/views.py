from django.shortcuts import render
from .models import Contacto
from .forms import Formulario 


def presentacion(request):
	return render(request,"presentacion.html",{})

def inicio(request):
	f=Formulario()
	context={
	"form":f
	}
	return render(request,"inicio.html",context)