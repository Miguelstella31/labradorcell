from django.shortcuts import render, get_object_or_404, redirect
from .models import OrdenReparacion
from .forms import OrdenReparacionForm

def lista_ordenes(request):
    ordenes = OrdenReparacion.objects.all()
    return render(request, 'reparaciones/lista_ordenes.html', {'ordenes': ordenes})

def crear_orden(request):
    if request.method == 'POST':
        form = OrdenReparacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ordenes')
    else:
        form = OrdenReparacionForm()
    return render(request, 'reparaciones/crear_orden.html', {'form': form})

def editar_orden(request, pk):
    orden = get_object_or_404(OrdenReparacion, pk=pk)
    if request.method == 'POST':
        form = OrdenReparacionForm(request.POST, instance=orden)
        if form.is_valid():
            form.save()
            return redirect('lista_ordenes')
    else:
        form = OrdenReparacionForm(instance=orden)
    return render(request, 'reparaciones/editar_orden.html', {'form': form})

def detalle_orden(request, pk):
    orden = get_object_or_404(OrdenReparacion, pk=pk)
    return render(request, 'reparaciones/detalle_orden.html', {'orden': orden})





