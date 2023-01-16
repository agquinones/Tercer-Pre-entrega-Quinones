from django.contrib import admin
from .models import Cliente,Operario,Mantenimiento

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Operario)
admin.site.register(Mantenimiento)
