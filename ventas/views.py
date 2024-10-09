# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Venta
from .forms import VentaForm  # Asegúrate de tener un formulario para manejar las ventas

# Vista para listar todas las ventas
def listar_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/listar_ventas.html', {'ventas': ventas})

# Vista para crear una nueva venta
def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_ventas')  # Redirige a la vista de listar ventas
    else:
        form = VentaForm()
    return render(request, 'ventas/crear_venta.html', {'form': form})

# Vista para editar una venta existente
def editar_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)
    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('listar_ventas')  # Redirige a la vista de listar ventas
    else:
        form = VentaForm(instance=venta)
    return render(request, 'ventas/editar_venta.html', {'form': form})

# Vista para eliminar una venta
def eliminar_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)
    if request.method == 'POST':
        venta.delete()
        return redirect('listar_ventas')  # Redirige a la vista de listar ventas
    return render(request, 'ventas/eliminar_venta.html', {'venta': venta})
