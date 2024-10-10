from django.shortcuts import render,redirect
from .models import Cliente
from .forms import ClienteForm  # Asegúrate de tener un formulario para manejar los clientes



def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')  # Redirige a la lista de clientes
    else:
        form = ClienteForm()
    return render(request, 'clientes/cliente_nuevo.html', {'form': form})