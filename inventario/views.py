from django.http import HttpResponse, HttpRequest, HttpResponseForbidden
from django.shortcuts import render
from django.template import loader
from .models import Proveedor
from django.urls import reverse

# Create your views here.

# region Proveedores
def proveedor(request:HttpRequest):
    if "usuario" not in request.session or not request.session["usuario"]:
        return HttpResponseForbidden(content=f"Acceso no permitido <br><a href=\"{reverse('signin')}\">Iniciar sesión</a>")
    id = request.GET.get('id')
    if Proveedor.objects.all().filter(id_proveedor=id):
        proveedor = Proveedor.objects.get(id_proveedor=id)
    else:
        proveedor = None
    template = loader.get_template('detalles_proveedor.html')

    context = {
        'proveedor':proveedor
    }
    return HttpResponse(template.render(context, request))

def proveedores(request:HttpRequest):
    if "usuario" not in request.session or not request.session["usuario"]:
        return HttpResponseForbidden(content=f"Acceso no permitido <br><a href=\"{reverse('signin')}\">Iniciar sesión</a>")
    proveedores = Proveedor.objects.all()
    template = loader.get_template('proveedores.html')

    context = {
        'proveedores':proveedores
    }
    return HttpResponse(template.render(context, request))

def guardar_proveedor(request:HttpRequest):
    if not request.session["usuario"] or request.method != 'POST':
        return HttpResponseForbidden(content=f"Acceso no permitido <br><a href=\"{reverse('signin')}\">Iniciar sesión</a>")
    new = Proveedor()
    data = request.POST
    # new.id_proveedor = last + 1
    nit = data.get('nit')
    new.nit = nit
    nombre = data.get('nombre')
    new.nombre = nombre
    direccion = data.get('direccion')
    new.direccion = direccion
    telefono = data.get('telefono')
    new.telefono = telefono
    categoria = data.get('categoria')
    new.categoria = categoria
    if nit and nombre and direccion and categoria and not Proveedor.objects.all().filter(nit=new.nit):
        new.save()
    template = loader.get_template('nuevo_proveedor.html')
    return HttpResponse(template.render({}, request))

def actualizar_proveedor(request:HttpRequest):
    if "usuario" not in request.session or not request.session["usuario"]:
        return HttpResponseForbidden(content=f"Acceso no permitido <br><a href=\"{reverse('signin')}\">Iniciar sesión</a>")
    id = request.GET.get('id')
    proveedor = None
    if Proveedor.objects.all().filter(id_proveedor=id):
        proveedor = Proveedor.objects.get(id_proveedor=id)
    template = loader.get_template('actualizar_proveedor.html')
    context = {
        'proveedor':proveedor
    }
    return HttpResponse(template.render(context, request))

def guardar_cambios_proveedor(request:HttpRequest):
    if not request.session["usuario"] or request.method != 'POST':
        return HttpResponseForbidden(content=f"Acceso no permitido <br><a href=\"{reverse('signin')}\">Iniciar sesión</a>")
    data = request.POST
    id = data.get('id')
    proveedor = Proveedor.objects.get(id_proveedor=id)
    nombre = data.get('nombre')
    proveedor.nombre = nombre if nombre else proveedor.nombre
    nit = data.get('nit')
    proveedor.nit = nit if nit else proveedor.nit
    direccion = data.get('direccion')
    proveedor.direccion = direccion if direccion else proveedor.direccion
    telefono = data.get('telefono')
    proveedor.telefono = telefono if telefono else proveedor.telefono
    categoria = data.get('categoria')
    proveedor.categoria = categoria if categoria else proveedor.categoria
    proveedor.save()

    template = loader.get_template('detalles_proveedor.html')
    context = {
        'proveedor':proveedor
    }
    return HttpResponse(template.render(context, request))

def nuevo_proveedor(request:HttpRequest):
    if "usuario" not in request.session or not request.session["usuario"]:
        return HttpResponseForbidden(content=f"Acceso no permitido <br><a href=\"{reverse('signin')}\">Iniciar sesión</a>")

    template = loader.get_template('nuevo_proveedor.html')
    context = {
        # "id":Proveedor.objects.all().count()+1,
    }
    return HttpResponse(template.render(context, request))

# endregion
