from django.contrib import admin
from .models import Proveedor, Producto  # Asegúrate de importar tus modelos

# Definición del modelo Proveedor en el panel de administración
@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'email', 'direccion')  # Campos a mostrar en la lista
    search_fields = ('nombre', 'telefono', 'email')  # Campos que se pueden buscar
    list_filter = ('nombre',)  # Filtros disponibles

    # Opcional: personalizar el formulario de edición
    fieldsets = (
        (None, {
            'fields': ('nombre', 'telefono', 'email', 'direccion', 'notas')
        }),
    )

# Definición del modelo Producto en el panel de administración
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'codigo_barras', 'proveedor')  # Campos a mostrar en la lista
    search_fields = ('nombre', 'codigo_barras')  # Campos que se pueden buscar
    list_filter = ('proveedor',)  # Filtros disponibles

    # Opcional: personalizar el formulario de edición
    fieldsets = (
        (None, {
            'fields': ('nombre', 'descripcion', 'precio', 'codigo_barras', 'imagen', 'proveedor')
        }),
    )

