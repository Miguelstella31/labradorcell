from django.db import models
from productos.models import Producto

class Inventario(models.Model):
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE)
    cantidad_disponible = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.producto.nombre} - {self.cantidad_disponible} unidades'

    def inventario_bajo(self):
        return self.cantidad_disponible < 10  # Ejemplo de alerta de stock bajo
