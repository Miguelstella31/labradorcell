from django.urls import path
from . import views

urlpatterns = [
    path('ordenes/', views.lista_ordenes, name='lista_ordenes'),
    path('ordenes/nueva/', views.crear_orden, name='crear_orden'),
    path('ordenes/editar/<int:pk>/', views.editar_orden, name='editar_orden'),
    path('ordenes/<int:pk>/', views.detalle_orden, name='detalle_orden'),
]
