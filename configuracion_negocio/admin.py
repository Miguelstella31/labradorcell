from django.contrib import admin
from .models import ConfiguracionNegocio, Empleado

@admin.register(ConfiguracionNegocio)
class ConfiguracionNegocioAdmin(admin.ModelAdmin):
    list_display = ('nombre_negocio', 'direccion', 'telefono', 'email', 'moneda')

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rol', 'telefono', 'email')
