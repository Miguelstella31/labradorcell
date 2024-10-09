from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'email', 'direccion', 'fecha_registro')
    search_fields = ('nombre', 'telefono', 'email')
    list_filter = ('fecha_registro',)

    fieldsets = (
        (None, {
            'fields': ('nombre', 'telefono', 'email', 'direccion', 'notas')
        }),
        ('Información adicional', {
            'fields': ('fecha_registro',),
            'classes': ('collapse',),
        }),
    )
    
    readonly_fields = ('fecha_registro',)  # Marca fecha_registro como de solo lectura
