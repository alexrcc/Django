from django.shortcuts import render
from .models import Contacto
from .forms import Formulario
from .forms import FormularioModeloA



def inicio(request):
	f=FormularioModeloA(request.POST or None)
	context={
	"titulo":"holaa",
	"form":f
	}

	if f.is_valid():
		f_data=f.cleaned_data
		n=f_data.get("nombres")
		a=f_data.get("apellidos")
		c=f_data.get("cedula")
		e=f_data.get("email")
		obj= Contacto.objects.create(nombres=n,apellidos=a,cedula=c, email=e)

		if obj:
			context={
				"titulo":"Se ha grabado correcatamente"
			
			}
	return render(request,"inicio.html",context)



