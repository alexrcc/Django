from django.shortcuts import render
from .forms import Formulario
from .models import CajaAhorros
from .models import Cliente

def listar(request):
	clientes = Cliente.objects.all()
	context={
		'clientes':clientes,
	}
	return render(request,"listar.html",context)
def crear(request):
	return render(request,"crear.html",{})
def modificar(request):
	return render(request,"modificar.html",{})