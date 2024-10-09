# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_ventas, name='listar_ventas'),
    path('crear/', views.crear_venta, name='crear_venta'),
    path('editar/<int:venta_id>/', views.editar_venta, name='editar_venta'),
    path('eliminar/<int:venta_id>/', views.eliminar_venta, name='eliminar_venta'),
]
