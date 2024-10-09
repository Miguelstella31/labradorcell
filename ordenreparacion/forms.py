from django import forms
from .models import OrdenReparacion

class OrdenReparacionForm(forms.ModelForm):
    class Meta:
        model = OrdenReparacion
        fields = [
            'imei', 'modelo', 'marca', 'falla_reportada',
            'prueba_carga', 'prueba_camara', 'prueba_microfono',
            'costo_reparacion', 'abono'
        ]
