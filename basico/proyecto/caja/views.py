from django.shortcuts import render
from .forms import FormularioCliente
from .forms import FormularioClienteModificar
from .models import CajaAhorros
from .models import Cliente
from reportlab.pdfgen import canvas
from django.http import HttpResponse

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
			cl = Cliente()
			cl.idCA= CajaAhorros.objects.all()[0]
			cl.nombres=f_data.get("nombres")
			cl.apellidos=f_data.get("apellidos")
			cl.cedula=f_data.get("cedula")
			cl.correo=f_data.get("correo")
			cl.telefono=f_data.get("telefono")
			cl.celular=f_data.get("celular")
			cl.direccion=f_data.get("direccion")
			cl.sexo=f_data.get("sexo")
			cl.estadoCivil=f_data.get("estadoCivil")
			cl.fechaNacimiento=f_data.get("fechaNacimiento")

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
	f=FormularioClienteModificar(request.POST or None)
	cedula=request.GET['cedula']
	cliente=Cliente.objects.get(cedula=cedula)

	f.fields['nombres'].initial = cliente.nombres
	f.fields['apellidos'].initial = cliente.apellidos
	f.fields['correo'].initial = cliente.correo
	f.fields['telefono'].initial = cliente.telefono
	f.fields['celular'].initial = cliente.celular
	f.fields['direccion'].initial = cliente.direccion
	f.fields['sexo'].initial = cliente.sexo
	f.fields['estadoCivil'].initial = cliente.estadoCivil
	f.fields['fechaNacimiento'].initial = cliente.fechaNacimiento

	if f.is_valid():
		f_data=f.cleaned_data
		cliente.nombres=f_data.get("nombres")
		cliente.apellidos=f_data.get("apellidos")
		cliente.correo=f_data.get("correo")
		cliente.telefono=f_data.get("telefono")
		cliente.celular=f_data.get("celular")
		cliente.direccion=f_data.get("direccion")
		cliente.sexo=f_data.get("sexo")
		cliente.estadoCivil=f_data.get("estadoCivil")
		cliente.fechaNacimiento=f_data.get("fechaNacimiento")
		cliente.save()

	context={
		'mod':'Modificar Cliente: '+cliente.nombres+"/"+cliente.cedula,
		'form':f,
	}

	return render(request,"modificar.html",context)

def pdf(request):
    response =HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'
    cedula=request.GET['cedula']
    cliente=Cliente.objects.get(cedula=cedula)
    p = canvas.Canvas(response)
    p.drawString(0, 0, "Nombre:")
    p.drawString(20, 0, "Apellido:")
    p.drawString(30, 0, "Cedula:")

    p.drawString(80, 100, cliente.nombres)
    p.drawString(100, 100, cliente.apellidos)
    p.drawString(200, 100, cliente.cedula)

    p.showPage()
    p.save()
    return response