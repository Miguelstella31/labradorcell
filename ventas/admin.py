from django.contrib import admin
from .models import Venta, DetalleVenta

# Inline para DetalleVenta dentro de Venta
class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 1  # Fila extra para agregar más detalles

# Configuración del panel para Venta
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'fecha', 'total')  # Asegúrate de que estos campos existen
    search_fields = ('cliente__nombre',)  # Verifica que Cliente tiene un campo 'nombre'
    list_filter = ('fecha',)  # Filtro por fecha
    inlines = [DetalleVentaInline]  # Agrega detalles de la venta en el mismo formulario

# Registrar los modelos
admin.site.register(Venta, VentaAdmin)
admin.site.register(DetalleVenta)

