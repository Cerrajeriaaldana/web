from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import ClienteForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages  # Importa el módulo de mensajes
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Cliente, Factura, DetalleVenta
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseForbidden


#Pestaña Principal
def Home_clientes(request):
    if "usuario" not in request.session or not request.session["usuario"]:
        return HttpResponseForbidden(content=f"Acceso no permitido <br><a href=\"{reverse('signin')}\">Iniciar sesión</a>")
    return render(request, "Home_clientes.html")


#Metodo Agregar Cliente
def agregar_cliente(request):
    if "usuario" not in request.session or not request.session["usuario"]:
        return HttpResponseForbidden(content=f"Acceso no permitido <br><a href=\"{reverse('signin')}\">Iniciar sesión</a>")
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente guardado con éxito')  # Agrega un mensaje de éxito
            return redirect('agregar_cliente')  # Redirige a la misma página
    else:
        form = ClienteForm()
    return render(request, 'agregateclient.html', {'form': form})


# Método Lista De Clientes
def lista_clientes(request):
    if "usuario" not in request.session or not request.session["usuario"]:
        return HttpResponseForbidden(content=f"Acceso no permitido <br><a href=\"{reverse('signin')}\">Iniciar sesión</a>")
    search_query = request.GET.get('search', '')  # Obtener el término de búsqueda del parámetro GET
    if search_query:
        clientes = Cliente.objects.filter(nombre__icontains=search_query).order_by('nombre')
    else:
        clientes = Cliente.objects.all().order_by('nombre')
    return render(request, "listClientes.html", {"clientes": clientes})



# Método Lista De Clientes con búsqueda


def About(request):
    return render(request, "about.html")

#Clientes
def cliente(request, id):
    if request.method == 'GET':
        cliente = Cliente.objects.filter(id=id).values('nit', 'nombre', 'direccion', 'telefono')
        return JsonResponse(list(cliente), safe=False)
    return HttpResponse("Método no permitido", status=405)


def buscar_cliente(request):
    if "usuario" not in request.session or not request.session["usuario"]:
        return HttpResponseForbidden(content=f"Acceso no permitido <br><a href=\"{reverse('signin')}\">Iniciar sesión</a>")
    query = request.GET.get('q')
    if query:
        clientes = Cliente.objects.filter(nombre__icontains=query)
    else:
        clientes = Cliente.objects.all()
    return render(request, 'buscar_clientes.html', {'clientes': clientes, 'query': query})


def detalles_cliente(request, nit):
    if "usuario" not in request.session or not request.session["usuario"]:
        return HttpResponseForbidden(content=f"Acceso no permitido <br><a href=\"{reverse('signin')}\">Iniciar sesión</a>")
    cliente = get_object_or_404(Cliente, nit=nit)
    facturas = []
    total = 0
    if Factura.objects.all().filter(cliente_id=cliente):
        facturas = Factura.objects.all().filter(cliente_id=cliente)
        if facturas:
            for factura in facturas:
                total += factura.total
    return render(
        request, 'detalles_cliente.html', 
        {
            'cliente': cliente,
            'facturas': facturas,
            'total': total
         }
         )



def modificar_cliente(request, nit):
    if "usuario" not in request.session or not request.session["usuario"]:
        return HttpResponseForbidden(content=f"Acceso no permitido <br><a href=\"{reverse('signin')}\">Iniciar sesión</a>")
    cliente = get_object_or_404(Cliente, nit=nit)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente modificado con éxito')
            # Redirige al usuario a la página de detalles del cliente después de guardar los cambios
            return redirect('detalles_cliente', nit=nit)
    else:
        form = ClienteForm(instance=cliente)
    
    return render(request, 'modificar_cliente.html', {'form': form, 'cliente': cliente})
