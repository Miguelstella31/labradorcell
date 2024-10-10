from django import forms
from .models import ConfiguracionNegocio, Empleado

class ConfiguracionNegocioForm(forms.ModelForm):
    class Meta:
        model = ConfiguracionNegocio
        fields = ['nombre_negocio', 'direccion', 'telefono', 'email', 'logo', 'moneda']

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'rol', 'telefono', 'email', 'usuario']

