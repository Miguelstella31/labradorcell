from django.test import TestCase
from .models import ConfiguracionNegocio, Empleado
from django.contrib.auth.models import User

class ConfiguracionNegocioTest(TestCase):
    def setUp(self):
        self.configuracion = ConfiguracionNegocio.objects.create(
            nombre_negocio="Labrador Cell",
            direccion="123 Calle Falsa",
            telefono="555-1234",
            email="labradorcell@example.com",
            moneda="USD"
        )

    def test_configuracion_negocio_str(self):
        self.assertEqual(str(self.configuracion), "Labrador Cell")

class EmpleadoTest(TestCase):
    def setUp(self):
        user = User.objects.create(username="johndoe")
        self.empleado = Empleado.objects.create(
            nombre="John Doe",
            rol="admin",
            telefono="555-4321",
            email="johndoe@example.com",
            usuario=user
        )

    def test_empleado_str(self):
        self.assertEqual(str(self.empleado), "John Doe - admin")

