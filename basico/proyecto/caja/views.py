from django.shortcuts import render
from .forms import Formulario
from .models import CajaAhorros

def listar(request):
	f=Formulario(request.POST or None)
	context={
	"form":f
	}
	return render(request,"listar.html",context)
def crear(request):
	return render(request,"crear.html",{})
def modificar(request):
	return render(request,"modificar.html",{})