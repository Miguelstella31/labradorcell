from django.shortcuts import render, get_object_or_404, redirect
from .models import Inventario
from productos.models import Producto

def lista_inventario(request):
    inventarios = Inventario.objects.all()  # Obtener todos los productos del inventario
    return render(request, 'inventario/lista_inventario.html', {'inventarios': inventarios})

def actualizar_inventario(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    
    if request.method == 'POST':
        cantidad_nueva = request.POST.get('cantidad_disponible')
        if cantidad_nueva.isdigit():  # Verificar si la cantidad es un número válido
            inventario.cantidad_disponible = int(cantidad_nueva)
            inventario.save()
            return redirect('lista_inventario')  # Redirigir a la lista de inventario después de actualizar
    return render(request, 'inventario/actualizar_inventario.html', {'inventario': inventario})
