from django.db import models

# Create your models here.

class Cliente(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()
    auto=models.CharField(max_length=40)
    
    
    def __str__(self):
        texto= '{0}, {1} ({2})'
        return texto.format(self.apellido, self.nombre, self.auto)


class Operario(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()
    profesion=models.CharField(max_length=40)

    def __str__(self):
        texto= '{0}, {1} ({2})'
        return texto.format(self.apellido, self.nombre, self.profesion)


class Mantenimiento(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=40)

    def __str__(self):
        return f"{self.nombre}"