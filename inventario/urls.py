from django.urls import path
from . import views

urlpatterns = [
    path('proveedor/', views.proveedor),
    path('proveedores/', views.proveedores, name='proveedores'),
    path('nuevo_proveedor/', views.nuevo_proveedor, name='nuevo_proveedor'),
    path('guardar_proveedor/', views.guardar_proveedor),
    path('actualizar_proveedor/', views.actualizar_proveedor),
    path('guardar_cambios_proveedor/', views.guardar_cambios_proveedor),
]
