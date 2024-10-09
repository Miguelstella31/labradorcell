from django.urls import path
from . import views
from .views import actualizar_inventario, lista_inventario

urlpatterns = [
    path('', views.lista_inventario, name='lista_inventario'),  # Ruta para ver la lista de inventario
    path('actualizar/<int:pk>/', views.actualizar_inventario, name='actualizar_inventario'),  # Ruta para actualizar un producto del inventario
    path('actualizar/', actualizar_inventario, name='actualizar_inventario'),
    path('', lista_inventario, name='lista_inventario'),
]
