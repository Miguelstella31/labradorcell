from django.db import models
from decimal import Decimal
from clientes.models import Cliente

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

    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Orden de Reparación - IMEI: {self.imei} - Marca: {self.marca} - Modelo: {self.modelo}"

    def saldo_pendiente(self):
        return Decimal(self.costo_reparacion) - Decimal(self.abono)