from django.shortcuts import render
from .forms import FormularioCliente
from .models import CajaAhorros
from .models import Cliente

def listar(request):
	clientes = Cliente.objects.all()
	context={
		'clientes':clientes,
	}
	return render(request,"listar.html",context)

def crear(request):
	f=FormularioCliente(request.POST or None)

	if request.method == 'POST':

		if f.is_valid():
			f_data=f.cleaned_data
			idCaja= CajaAhorros.objects.all()[0]
			n=f_data.get("nombres")
			a=f_data.get("apellidos")
			c=f_data.get("cedula")
			co=f_data.get("correo")
			t=f_data.get("telefono")
			celu=f_data.get("celular")
			direc=f_data.get("direccion")
			sex=f_data.get("sexo")
			ec=f_data.get("estadoCivil")
			fn=f_data.get("fechaNacimiento")

			obj=Cliente.objects.create(idCA=idCaja, nombres=n,apellidos=a,cedula=c,correo=co, telefono=t, celular=celu, direccion=direc, sexo=sex, estadoCivil=ec, fechaNacimiento=fn )
			if obj:
				clientes=Cliente.objects.all()
				context={
					'clientes':clientes,
				}
				return render(request,"listar.html",context)
	context={
		"form":f,
	}
	return render(request,"crear.html",context)
	

def modificar(request):
	return render(request,"modificar.html",{})