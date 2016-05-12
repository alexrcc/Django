from django.shortcuts import render
from .models import Contacto


def presentacion(request):
	return render(request,"presentacion.html",{})

