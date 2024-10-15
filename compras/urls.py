from django.urls import path
from . import views

urlpatterns = [
    path('compra/', views.compra, name='nueva_compra'),
    path('compra/detalle/', views.detalle_compra, name='detalle_compra'),
    path('compras/', views.compras, name='compras'),
    path('compra/guardar_compra/', views.guardar_compra, name='guardar_compra'),
]
