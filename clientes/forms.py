from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono', 'direccion', 'notas']  # Excluir 'fecha_registro'

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        # Añadir manualmente el campo 'fecha_registro' al formulario
        self.fields['fecha_registro'] = forms.DateTimeField(
            label='Fecha de Registro', 
            initial=self.instance.fecha_registro, 
            disabled=True,  # Hacerlo no editable
            required=False
        )

