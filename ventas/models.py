from django.db import models
from clientes.models import Cliente
from productos.models import Producto

# Modelo de Venta
class Venta(models.Model):
    id = models.AutoField(primary_key=True)  # Añade esta línea para definir explícitamente el campo id
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Venta {self.id} - {self.cliente.nombre}'


# Modelo de DetalleVenta
class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.cantidad}x {self.producto.nombre}'

    @property
    def subtotal(self):
        return self.cantidad * self.precio_unitario
