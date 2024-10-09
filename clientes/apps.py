from django.apps import AppConfig


class ClientesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clientes'
    def ready(self):
    # Optional: Perform actions when the app is ready (e.g., signals)
     pass



