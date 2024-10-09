from django.urls import path
from . import views

urlpatterns = [
    path('proveedores/', views.lista_proveedores, name='lista_proveedores'),
    path('proveedores/nuevo/', views.crear_proveedor, name='crear_proveedor'),
    path('proveedores/editar/<int:pk>/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedores/eliminar/<int:pk>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('proveedores/<int:proveedor_id>/productos/', views.productos_por_proveedor, name='productos_por_proveedor'),
    path('productos/nuevo/', views.nuevo_producto, name='nuevo_producto'),
]
