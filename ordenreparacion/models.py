from django.db import models
from decimal import Decimal
from clientes.models import Cliente
import uuid  # Importar para generar un UUID

class OrdenReparacion(models.Model):
    ESTADO_PRUEBAS = [
        ('FUNCIONA', 'Funciona'),
        ('NO_FUNCIONA', 'No Funciona'),
        ('NO_APLICA', 'No Aplica'),
    ]
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    imei = models.CharField(max_length=15, unique=True, verbose_name='IMEI')
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    falla_reportada = models.TextField(verbose_name='Descripción de la falla')
    
    # Pruebas básicas
    prueba_carga = models.CharField(max_length=11, choices=ESTADO_PRUEBAS, default='NO_APLICA')
    prueba_camara = models.CharField(max_length=11, choices=ESTADO_PRUEBAS, default='NO_APLICA')
    prueba_microfono = models.CharField(max_length=11, choices=ESTADO_PRUEBAS, default='NO_APLICA')
    
    # Información de costos
    costo_reparacion = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Costo Total de Reparación')
    abono = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Abono', default=Decimal('0.00'))
    
    # Nuevo campo para el número de orden
    numero_orden = models.CharField(max_length=20, unique=True, default='', blank=True)  # Inicialmente vacío
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.numero_orden:  # Generar número de orden solo si está vacío
            self.numero_orden = str(uuid.uuid4().int)[:20]  # Genera un UUID único truncado a 20 caracteres
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Orden de Reparación - IMEI: {self.imei} - Marca: {self.marca} - Modelo: {self.modelo}"

    def saldo_pendiente(self):
        return Decimal(self.costo_reparacion) - Decimal(self.abono)

