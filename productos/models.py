from django.db import models

# Función para obtener el proveedor predeterminado
def get_default_proveedor():
    return Proveedor.objects.first()  # Ajusta esto según cómo quieras seleccionar el proveedor

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    direccion = models.TextField()
    notas = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    codigo_barras = models.CharField(max_length=13, unique=True)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    
    # Clave foránea con proveedor predeterminado mediante una función
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, default=get_default_proveedor)

    def __str__(self):
        return self.nombre




    
