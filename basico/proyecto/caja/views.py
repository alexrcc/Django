from django.shortcuts import render

def listar(request):
	return render(request,"listar.html",{})
def crear(request):
	return render(request,"crear.html",{})
def modificar(request):
	return render(request,"modificar.html",{})