from django.shortcuts import render
from .models import Cliente,Operario,Mantenimiento

# Create your views here.

def home(request):
    clienteslistados = Cliente.objects.all()
    return render(request,"index.html",{"clientes":clienteslistados})