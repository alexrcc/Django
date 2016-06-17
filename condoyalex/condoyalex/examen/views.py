from django.shortcuts import render, redirect
from .models import Producto, Compra
from .forms import FormularioCompra
from django.contrib import messages

# Create your views here.
def listar(request):
	prod = Producto.objects.all()
	context={
		'prod':prod,
	}
	return render(request,"listar.html",context)

def comprar(request):
	prod=request.GET['nombre']
	producto=Producto.objects.get(nombre=prod)
	f=FormularioCompra(request.POST or None)
	context={
		'mod':'Compra de Producto: '+producto.nombre,
		'precio': " Precio: "+str(producto.precio),
		'can':" cantidad maxima de compra: "+str(producto.stock),
		'form':f,
	}
	if request.method == 'POST':
		if f.is_valid():
			f_data=f.cleaned_data
			com=Compra()
			com.cant=f_data.get("cant")
			com.idPro=producto
			if(producto.stock<f_data.get("cant")):
				messages.add_message(request, messages.ERROR, "No se pudo comprar porque la cantidad ingresada en mayor al STOCK", fail_silently=True)
				return redirect("/listar/comprar?nombre="+prod)
			if(f_data.get("cant")<1):
					messages.add_message(request, messages.ERROR, "No se pudo comprar porque la cantidad ingresada es incorrecta", fail_silently=True)
					return redirect("/listar/comprar?nombre="+prod)
			else:
		
				if (com.save() != True):
					producto.stock=producto.stock-f_data.get("cant")
					producto.save()
					if(producto.stock==0):
						producto.delete()
					return redirect(listar)
	
	return render(request,"comprar.html",context)

	