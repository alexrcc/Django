from django.shortcuts import render, redirect
from .models import Inscribir
from .forms import Formulario
from .forms import FormularioEditar
# Create your views here.
def inicio(request):
	clientes = Inscribir.objects.all()
	context={
		'clientes':clientes,
	}
	return render(request,"inicio.html",context)
def inscribir(request):
	f=Formulario(request.POST or None)
	context={
		'form':f,
	}

	if request.method == 'POST':

		if f.is_valid():
			f_data=f.cleaned_data
			
			n=f_data.get("nombres")
			a=f_data.get("apellidos")
			c=f_data.get("cedula")
			co=f_data.get("email")
			
			obj=Inscribir.objects.create(nombres=n,apellidos=a,cedula=c,email=co)
			if obj:
				datos=Inscribir.objects.all()
				context={
					'clientes':datos,
				}
				return redirect(inicio)
	context={
		"form":f,
	}
	return render(request,"inscribir.html",context)

def modificar(request):
	f=FormularioEditar(request.POST or None)
	cedula=request.GET['cedula']
	cliente=Inscribir.objects.get(cedula=cedula)

	f.fields['nombres'].initial = cliente.nombres
	f.fields['apellidos'].initial = cliente.apellidos
	f.fields['email'].initial = cliente.email
	context={
		'mod':'Modificar Cliente: '+cliente.nombres+"/"+cliente.cedula,
		'form':f,
	}
	if request.method == 'POST':
		if f.is_valid():
			f_data=f.cleaned_data
			cliente.nombres=f_data.get("nombres")
			cliente.apellidos=f_data.get("apellidos")
			cliente.email=f_data.get("email")
			
			m=cliente.save()
			return redirect(inicio)
	

	return render(request,"modificar.html",context)