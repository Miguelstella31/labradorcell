from django.db import models

class ConfiguracionNegocio(models.Model):
    nombre_negocio = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    moneda = models.CharField(max_length=10, default='USD')

    def __str__(self):
        return self.nombre_negocio

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)  # Ejemplo: 'admin', 'vendedor'
    telefono = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    usuario = models.OneToOneField('auth.User', on_delete=models.CASCADE)  # Relacionar con el usuario del sistema

    def __str__(self):
        return f'{self.nombre} - {self.rol}'
