from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.http import HttpRequest
from django.template import loader
from .models import Compra, Producto, DetalleCompra, Proveedor, Usuario
from django.urls import reverse

# Create your views here.
def compra(request):
    if "usuario" not in request.session or not request.session["usuario"]:
        return HttpResponseForbidden(content=f"Acceso no permitido <br><a href=\"{reverse('signin')}\">Iniciar sesión</a>")
    context = {
        'id':Compra.objects.count() + 1,
        'productos': Producto.objects.all(),
        'proveedores': Proveedor.objects.all(),
        'usuario': 'adm1'
    }
    return render(request, 'compra.html', context)

def detalle_compra(request):
    if "usuario" not in request.session or not request.session["usuario"]:
        return HttpResponseForbidden(content=f"Acceso no permitido <br><a href=\"{reverse('signin')}\">Iniciar sesión</a>")
    id = request.GET.get("id")
    if Compra.objects.filter(id=id):
        compra = Compra.objects.get(id=id)
        detalles = DetalleCompra.objects.filter(compra_numero=compra)
    else:
        compra = None
        detalles = None
    template = loader.get_template('detalles_compra.html')
    context = {
        'compra': compra,
        'detalles': detalles
    }
    return HttpResponse(template.render(context, request))


def guardar_compra(request:HttpRequest):
    if not request.session["usuario"] or request.method != 'POST':
        return HttpResponseForbidden(content=f"Acceso no permitido <br><a href=\"{reverse('signin')}\">Iniciar sesión</a>")
    usuario = request.session["usuario"]
    data = request.POST
    id = Compra.objects.count() + 1
    nueva_compra = Compra()
    nueva_compra.numero = id
    nueva_compra.id_proveedor = Proveedor.objects.get(id_proveedor=data.get('id_proveedor'))
    nueva_compra.fecha = data.get('fecha')
    nueva_compra.total = data.get('total')
    nueva_compra.usuario = Usuario.objects.get(usuario=usuario)
    productos = [key for key in data.keys() if key.startswith('producto')]
    if productos:
        nueva_compra.save()
        for key in productos:
            detalle = DetalleCompra()
            detalle.compra_numero = nueva_compra
            producto = Producto.objects.get(id_producto=key.split('_')[1])
            detalle.id_producto = producto
            detalle.cantidad = data.get(key)
            # producto.existencia += int(data.get(key))
            detalle.precio_unitario = Producto.objects.get(id_producto=key.split('_')[1]).precio
            detalle.precio_por_mayor = Producto.objects.get(id_producto=key.split('_')[1]).precio
            producto.save()
            detalle.save()
    return HttpResponse('Compra guardada con exito<br><a href="/compras">Ver todas</a>')

def compras(request):
    if "usuario" not in request.session or not request.session["usuario"]:
        return HttpResponseForbidden(content=f"Acceso no permitido <br><a href=\"{reverse('signin')}\">Iniciar sesión</a>")
    compras = Compra.objects.all()
    # breakpoint()
    detalles = DetalleCompra.objects.all()
    total = 0 
    for compra in compras:
        total += compra.total
    context = {
        'compras': compras,
        'detalles': detalles,
        'total': total,
    }
    return render(request, 'compras.html', context)