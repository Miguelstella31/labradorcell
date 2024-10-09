from django import forms
from .models import Venta# Importa el modelo Venta, no Ventas

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta # Asegúrate de que el modelo aquí sea Venta, como está en models.py
        fields = '__all__'  # O especifica los campos que quieres incluir

