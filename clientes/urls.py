# clientes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),  # Asegúrate de usar el nombre correcto
    path('nuevo/', views.crear_cliente, name='crear_cliente'),
]


