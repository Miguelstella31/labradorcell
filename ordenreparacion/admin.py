from django.contrib import admin
from .models import OrdenReparacion  # Importa tu modelo

@admin.register(OrdenReparacion)
class OrdenReparacionAdmin(admin.ModelAdmin):
    list_display = ('imei', 'marca', 'modelo', 'costo_reparacion', 'abono', 'fecha_creacion', 'saldo_pendiente')  # Campos a mostrar en la lista
    search_fields = ('imei', 'marca', 'modelo')  # Campos que se pueden buscar
    list_filter = ('marca', 'modelo', 'prueba_carga', 'prueba_camara', 'prueba_microfono')  # Filtros disponibles
    ordering = ('-fecha_creacion',)  # Ordenar por fecha de creación (más reciente primero)

    # Opcional: personalizar el formulario de edición
    fieldsets = (
        (None, {
            'fields': ('imei', 'marca', 'modelo', 'falla_reportada', 'prueba_carga', 'prueba_camara', 'prueba_microfono', 'costo_reparacion', 'abono')
        }),
        ('Fechas', {
            'fields': ('fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',),  # Opcional: colapsar el campo
        }),
    )
    
    # Añadir los campos como solo lectura
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion', 'saldo_pendiente')

    def saldo_pendiente(self, obj):
        """Calcula el saldo pendiente."""
        return obj.saldo_pendiente()
    saldo_pendiente.short_description = 'Saldo Pendiente'
