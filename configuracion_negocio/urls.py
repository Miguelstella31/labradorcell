from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Página de inicio
    path('configuracion/', views.configuracion_negocio, name='configuracion_negocio'),
    path('empleados/', views.lista_empleados, name='lista_empleados'),
    path('empleados/nuevo/', views.nuevo_empleado, name='nuevo_empleado'),
]
