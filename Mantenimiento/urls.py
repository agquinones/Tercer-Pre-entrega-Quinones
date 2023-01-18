from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.buscarcliente, name='home'),
    path('buscarcliente/', views.buscarcliente),
    path('cliente/', views.cliente, name='cliente'),
    path('operario/', views.operario, name='operario'),
    path('mantenimiento/', views.mantenimiento, name='mantenimiento'),
    path('registrarcliente/', views.registrarCliente),
    path('registraroperario/', views.registrarOperario),
    path('registrarmantenimiento/', views.registrarMantenimiento),
    path('cliente/edicioncliente/<codigo>', views.edicionCliente),
    path('operario/edicionoperario/<codigo>', views.edicionOperario),
    path('mantenimiento/edicionmantenimiento/<codigo>', views.edicionMantenimiento),
    path('cliente/eliminarcliente/<codigo>', views.eliminarCliente),
    path('operario/eliminaroperario/<codigo>', views.eliminarOperario),
    path('mantenimiento/eliminarmantenimiento/<codigo>', views.eliminarMantenimiento),
    path('editarcliente/', views.editarCliente),
    path('editaroperario/', views.editarOperario),
    path('editarmantenimiento/', views.editarMantenimiento),
]