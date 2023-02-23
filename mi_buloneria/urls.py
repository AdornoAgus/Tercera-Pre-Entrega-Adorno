from django.contrib import admin
from django.urls import path
from mi_buloneria import views



urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('proveedores',views.proveedor, name='proveedores'),
    path('deposito',views.deposito_, name='deposito'),
    path('cliente',views.cliente, name='cliente'),
    
]
