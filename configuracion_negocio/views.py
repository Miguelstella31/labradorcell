from django.shortcuts import render, redirect
from .models import ConfiguracionNegocio, Empleado
from .forms import ConfiguracionNegocioForm, EmpleadoForm
from django.views import View

def inicio(request):
    print("La vista inicio ha sido llamada")  # Para depuración
    return render(request, 'configuracion_negocio/inicio.html')

def configuracion_negocio(request):
    if request.method == 'POST':
        form = ConfiguracionNegocioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('configuracion_negocio')
    else:
        form = ConfiguracionNegocioForm()
    return render(request, 'configuracion_negocio/configuracion.html', {'form': form})

def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'configuracion_negocio/lista_empleado.html', {'empleados': empleados})

def nuevo_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'configuracion_negocio/nuevo_empleado.html', {'form': form})


