from django.shortcuts import render
from .models import Contacto
from .forms import Formulario 


def inicio(request):
	f=Formulario(request.POST or None)
	context={
	"form":f
	}
	return render(request,"inicio.html",context)

def presentacion(request):
	return render(request,"presentacion.html",{})
