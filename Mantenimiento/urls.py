from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarcliente/', views.registrarCliente),
    path('edicioncliente/<codigo>', views.edicionCliente),
    path('editarcliente/', views.editarCliente),
    path('eliminarcliente/<codigo>', views.eliminarCliente),
]