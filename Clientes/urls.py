from django.urls import path
from . import views

urlpatterns = [

    path("clientes/", views.Home_clientes),
    path("agre/", views.agregar_cliente, name="agregar_cliente"),
    path("cliente/<int:id>", views.cliente),
    path("list/", views.lista_clientes, name="lista_clientes"),
    path('buscar-cliente/', views.buscar_cliente, name='buscar_cliente'),
    path('cliente/<str:nit>/', views.detalles_cliente, name='detalles_cliente'),
    path('modificar-cliente/<str:nit>/', views.modificar_cliente, name='modificar_cliente'),
]



