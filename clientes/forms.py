# clientes/forms.py
from django import forms
from .models import Cliente  # Asegúrate de importar tu modelo

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email' ,'telefono','direccion','fecha_registro','notas',]  # Reemplaza con los campos que tengas en tu modelo
