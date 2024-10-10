"""
URL configuration for labradorcell project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]"""

# Archivo: urls.py
from django.urls import path
from . import views  # Importamos el archivo views
from django.contrib import admin
from django.urls import include, path  # Asegúrate de importar 'include'
from . import views  # Asegúrate de que el archivo views.py exista

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el panel de administración

    # Prefijos únicos para cada aplicación
    path('clientes/', include('clientes.urls')),  # URLs de la aplicación clientes
    path('ventas/', include('ventas.urls')),  # URLs de la aplicación ventas
    path('productos/', include('productos.urls')),  # URLs de la aplicación productos
    path('ordenes/', include('ordenreparacion.urls')),  # URLs de la aplicación de órdenes de reparación
    path('inventario/', include('inventario.urls')),  # URLs de la aplicación inventario
    path('', include('configuracion_negocio.urls')),  # Página principal con la configuración del negocio
]