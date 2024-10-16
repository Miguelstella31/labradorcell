from django.shortcuts import render, redirect
from .models import Cliente  # Asegúrate de importar correctamente
from .forms import ClienteForm

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')  # Redirige a la lista de clientes después de guardar
    else:
        form = ClienteForm()
    return render(request, 'clientes/cliente_nuevo.html', {'form': form})
