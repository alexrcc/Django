from django.shortcuts import render, redirect
from .forms import FormularioCliente, FormularioTransaccion
from .forms import FormularioClienteModificar
from .models import CajaAhorros, Transaccion
from .models import Cliente, CuentaAhorros
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

@login_required(login_url="/inicio")
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

			if (cl.save() != True):
				cuenta=CuentaAhorros()
				cuenta.idC=cl
				cuenta.numeroCuenta=(len(CuentaAhorros.objects.all()))+1
				cuenta.estado=True
				cuenta.saldo=0
				cuenta.save()
				return redirect(listar)
	context={
		"form":f,
	}
	return render(request,"crear.html",context)
def modificar(request):
	f=FormularioClienteModificar(request.POST or None)
	cedula=request.GET['cedula']
	cliente=Cliente.objects.get(cedula=cedula)
	context={
		'mod':'Modificar Cliente: '+cliente.nombres+"/"+cliente.cedula,
		'form':f,
	}

	f.fields['nombres'].initial = cliente.nombres
	f.fields['apellidos'].initial = cliente.apellidos
	f.fields['correo'].initial = cliente.correo
	f.fields['telefono'].initial = cliente.telefono
	f.fields['celular'].initial = cliente.celular
	f.fields['direccion'].initial = cliente.direccion
	f.fields['sexo'].initial = cliente.sexo
	f.fields['estadoCivil'].initial = cliente.estadoCivil
	f.fields['fechaNacimiento'].initial = cliente.fechaNacimiento
	if request.method == 'POST':
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
			return redirect(listar)
	

	return render(request,"modificar.html",context)

def pdf(request):
    response =HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'
    cedula=request.GET['cedula']
    cliente=Cliente.objects.get(cedula=cedula)
    p = canvas.Canvas(response)
    p.drawString(300, 800, "DATOS CLIENTE")
    p.drawString(20, 750, "Nombre:")
    p.drawString(20, 730, "Apellido:")
    p.drawString(20, 710, "Cedula:")
    p.drawString(20, 690, "Correo:")
    p.drawString(20, 670, "Telefono:")
    p.drawString(20, 650, "Celular:")
    p.drawString(20, 630, "Dirección:")
    p.drawString(20, 610, "Sexo:")
    p.drawString(20, 590, "Estado Civil:")
    p.drawString(20, 570, "Fecha de Nacimiento:")

    p.drawString(150, 750, cliente.nombres)
    p.drawString(150, 730, cliente.apellidos)
    p.drawString(150, 710, cliente.cedula)
    p.drawString(150, 690, cliente.correo)
    p.drawString(150, 670, cliente.telefono)
    p.drawString(150, 650, cliente.celular)
    p.drawString(150, 630, cliente.direccion)
    p.drawString(150, 610, cliente.sexo)
    p.drawString(150, 590, cliente.estadoCivil)
    t=cliente.fechaNacimiento
    p.drawString(150, 570,t.strftime('%m/%d/%Y'))

    p.showPage()
    p.save()
    return response
def eliminar(request):
	cedula=request.GET['cedula']
	cliente=Cliente.objects.get(cedula=cedula)
	falg=cliente.delete()
	if falg:
		clientes=Cliente.objects.all()
		context={
			'clientes':clientes,
		}
		return redirect(listar)
		
def loguear(request):
	f=AuthenticationForm(request.POST or None)
	context={
		'form':f,
	}
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		usuario = authenticate(username=username, password=password)
		if usuario is not None:
			if usuario.is_active:
				login(request,usuario)
				return redirect(listar)
			else:
				p="malo"
		else:
			p="mas malo"
		context={
		'error':p,
	}
	return render(request,"login.html",context)   

def cuenta(request):
	f=FormularioTransaccion(request.POST or None)
	ban=True


	
	if request.method == 'POST':

		ced=request.POST['ci']
		cuent=request.POST['cuenta']
		cu=CuentaAhorros.objects.get(numeroCuenta=cuent)
		if f.is_valid():
			f_data=f.cleaned_data
			if f_data.get("tipo")=='d':
				
				cu.saldo=cu.saldo+f_data.get("valor")
			if f_data.get("tipo")=='r':
				
				cu.saldo=cu.saldo-f_data.get("valor")

			if (cu.save() != True):
				T = Transaccion()
				T.idCuenta= cu
				T.tipo=f_data.get("tipo")
				T.valor=f_data.get("valor")
				T.save()
		return redirect("/caja/cuentas?cedula="+ced)
			
	else:
		cedula=request.GET['cedula']
		cliente=Cliente.objects.get(cedula=cedula)
		cuenta=CuentaAhorros.objects.filter(idC=cliente)
		context={
			'ft':f,
			'cuenta':cuenta,
			'cliente':cliente,
		}
	return render(request,"cuentas.html",context)

def GestionEstado(request):
	ced=request.GET['cedula']
	cuenta=request.GET['cuenta']
	c= CuentaAhorros.objects.get(numeroCuenta=cuenta)

	if(c.estado==True):
		c.estado=False
	else:
		c.estado=True
	c.save()
	return redirect("/caja/cuentas?cedula="+ced)

def NuevaCuenta(request):
	ced=request.GET['cedula']
	cl=Cliente.objects.get(cedula=ced)
	cuenta=CuentaAhorros()
	cuenta.idC=cl
	cuenta.numeroCuenta=(len(CuentaAhorros.objects.all()))+1
	cuenta.estado=True
	cuenta.saldo=0
	cuenta.save()
	return redirect("/caja/cuentas?cedula="+ced)

