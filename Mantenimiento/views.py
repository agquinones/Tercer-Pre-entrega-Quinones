from django.shortcuts import render, redirect
from .models import Cliente,Operario,Mantenimiento

# Create your views here.
def home(request):
    clienteslistados = Cliente.objects.all()
    return render(request,"index.html",{"clientes":clienteslistados})

def registrarCliente(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    apellido=request.POST['txtApellido']
    email=request.POST['txtEmail']
    auto=request.POST['txtAuto']
    cliente = Cliente.objects.create(codigo=codigo, nombre=nombre, apellido=apellido, email=email, auto=auto)
    return redirect('/')

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
    Cliente.nombre=nombre
    Cliente.apellido=apellido
    Cliente.email=email
    Cliente.auto=auto
    Cliente.save()
    return redirect('/')

def eliminarCliente(request, codigo):
    cliente= Cliente.objects.get(codigo=codigo)
    cliente.delete()
    return redirect('/')