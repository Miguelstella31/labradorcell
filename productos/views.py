from django.shortcuts import render, redirect
from .models import Proveedor
from .forms import ProveedorForm, ProductoForm 
from .models import Producto

def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'productos/crear_proveedor.html', {'form': form})

def editar_proveedor(request, pk):
    proveedor = Proveedor.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'productos/editar_proveedor.html', {'form': form})

def eliminar_proveedor(request, pk):
    proveedor = Proveedor.objects.get(pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('lista_proveedores')
    return render(request, 'productos/eliminar_proveedor.html', {'proveedor': proveedor})

# Crear la vista lista_proveedores
def lista_proveedores(request):
    proveedores = Proveedor.objects.all()  # Aquí puedes obtener la lista de proveedores de la base de datos
    return render(request, 'productos/lista_proveedores.html', {'proveedores': proveedores})


def productos_por_proveedor(request, proveedor_id):
    proveedor = Proveedor.objects.get(pk=proveedor_id)
    productos = Producto.objects.filter(proveedor=proveedor)
    return render(request, 'productos/reporte_productos.html', {'proveedor': proveedor, 'productos': productos})

def nuevo_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')  # Asegúrate de que esta URL exista
    else:
        form = ProductoForm()
    return render(request, 'productos/nuevo_producto.html', {'form': form})
