from django.shortcuts import render, get_object_or_404, redirect
from .models import OrdenReparacion
from .forms import OrdenReparacionForm
from django.contrib import messages


from django.shortcuts import render
from .forms import OrdenReparacionForm  # Asegúrate de que tu formulario esté importado

def crear_orden(request):
    if request.method == 'POST':
        form = OrdenReparacionForm(request.POST)
        if form.is_valid():
            # Guardar la orden de reparación
            form.save()
            return redirect('lista_ordenes')  # Redirigir después de guardar
    else:
        form = OrdenReparacionForm()

    return render(request, 'ordenreparacion/crear_orden.html', {'form': form})




def editar_orden(request, pk):
    orden = get_object_or_404(OrdenReparacion, pk=pk)
    
    if request.method == 'POST':
        form = OrdenReparacionForm(request.POST, instance=orden)
        if form.is_valid():
            form.save()
            messages.success(request, 'Orden editada exitosamente.')
            return redirect('lista_ordenes')
        else:
            messages.error(request, 'Hubo un error al editar la orden.')
    else:
        form = OrdenReparacionForm(instance=orden)
    
    return render(request, 'ordenreparacion/editar_orden.html', {'form': form})




def detalle_orden(request, pk):
    orden = get_object_or_404(OrdenReparacion, pk=pk)
    return render(request, 'ordenreparacion/detalle_orden.html', {'orden': orden})

def lista_ordenes(request):
    ordenes = OrdenReparacion.objects.all()
    return render(request, 'ordenreparacion/lista_ordenes.html', {'ordenes': ordenes})







