from django.shortcuts import render, redirect
from .models import Cliente,Operario,Mantenimiento

# Create your views here.

def home(request):
    return render(request,"index.html")

def buscarcliente(request):
    busqueda = request.GET.get('txtCodigo')
    clienteslistados = Cliente.objects.all()
    if busqueda:
        clienteslistados = Cliente.objects.filter(codigo__icontains = busqueda)
    return render(request, 'index.html',{'clientes':clienteslistados})

# ----- clientes -----

def cliente(request):
    clienteslistados = Cliente.objects.all()
    return render(request,"clientes.html",{"clientes":clienteslistados})

def registrarCliente(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    apellido=request.POST['txtApellido']
    email=request.POST['txtEmail']
    auto=request.POST['txtAuto']
    cliente = Cliente.objects.create(codigo=codigo, nombre=nombre, apellido=apellido, email=email, auto=auto)
    return redirect('/cliente/')

def edicionCliente(request, codigo):
    cliente= Cliente.objects.get(codigo=codigo)
    return render(request, "edicioncliente.html",{"cliente":cliente})

def editarCliente(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    apellido=request.POST['txtApellido']
    email=request.POST['txtEmail']
    auto=request.POST['txtAuto']
    cliente= Cliente.objects.get(codigo=codigo)
    cliente.nombre=nombre
    cliente.apellido=apellido
    cliente.email=email
    cliente.auto=auto
    cliente.save()
    return redirect('/cliente/')

def eliminarCliente(request, codigo):
    cliente= Cliente.objects.get(codigo=codigo)
    cliente.delete()
    return redirect('/cliente/')

# ----- operarios -----

def operario(request):
    operarioslistados = Operario.objects.all()
    return render(request,"operarios.html",{"operario":operarioslistados})

def registrarOperario(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    apellido=request.POST['txtApellido']
    email=request.POST['txtEmail']
    profesion=request.POST['txtProfesion']
    operario = Operario.objects.create(codigo=codigo, nombre=nombre, apellido=apellido, email=email, profesion=profesion)
    return redirect('/operario/')

def edicionOperario(request, codigo):
    operario= Operario.objects.get(codigo=codigo)
    return render(request, "edicionoperario.html",{"operario":operario})

def editarOperario(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    apellido=request.POST['txtApellido']
    email=request.POST['txtEmail']
    profesion=request.POST['txtProfesion']
    operario= Operario.objects.get(codigo=codigo)
    operario.nombre=nombre
    operario.apellido=apellido
    operario.email=email
    operario.profesion=profesion
    operario.save()
    return redirect('/operario/')

def eliminarOperario(request, codigo):
    operario= Operario.objects.get(codigo=codigo)
    operario.delete()
    return redirect('/operario/')

# ----- mantenimientos -----

def mantenimiento(request):
    mantenimientoslistados = Mantenimiento.objects.all()
    return render(request,"mantenimientos.html",{"mantenimiento":mantenimientoslistados})

def registrarMantenimiento(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    mantenimiento = Mantenimiento.objects.create(codigo=codigo, nombre=nombre)
    return redirect('/mantenimiento/')

def edicionMantenimiento(request, codigo):
    mantenimiento= Mantenimiento.objects.get(codigo=codigo)
    return render(request, "edicionmantenimiento.html",{"mantenimiento":mantenimiento})

def editarMantenimiento(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    mantenimiento= Mantenimiento.objects.get(codigo=codigo)
    mantenimiento.nombre=nombre
    mantenimiento.save()
    return redirect('/mantenimiento/')

def eliminarMantenimiento(request, codigo):
    mantenimiento= Mantenimiento.objects.get(codigo=codigo)
    mantenimiento.delete()
    return redirect('/mantenimiento/')