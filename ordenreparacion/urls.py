from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_ordenes, name='lista_ordenes'),  # Aquí no se necesita 'ordenes/'
    path('nueva/', views.crear_orden, name='crear_orden'),
    path('editar/<int:pk>/', views.editar_orden, name='editar_orden'),
    path('<int:pk>/', views.detalle_orden, name='detalle_orden'),
]
