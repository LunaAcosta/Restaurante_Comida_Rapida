from django.db import models

# Create your models here.

class Sucursal(models.Model):
    nombre = models.CharField(max_length = 30)
    direccion = models.CharField(max_length = 200)
    telefono = models.CharField(max_length = 8)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    nombre = models.CharField(max_length = 30)
    apellio = models.CharField(max_length = 30)
    puesto = models.CharField(max_length = 30)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    horario = models.TimeField(null = True)

    def __str__(self):
        return self.nombre+' '+ self.apellio+ ' Puesto: '+self.puesto

class Proveedor(models.Model):
    nombre = models.CharField(max_length = 30)
    direccion = models.CharField(max_length = 200) 
    telefono = models.CharField(max_length = 8) 

    def __str__(self):
        return self.nombre+ ' Telefono: ' +self.telefono


class TipoCarne(models.Model):
    tipoCarme = models.CharField(max_length = 30)

    def __str__(self):
        return self.tipoCarme

class Hamburguesas(models.Model):
    nombre = models.CharField(max_length = 30)
    tipoCarme = models.ForeignKey(TipoCarne, on_delete = models.CASCADE)
    tamaño = models.CharField(max_length = 20)
    numeroCarne = models.CharField(max_length = 20)
    vegetales = models.CharField(max_length = 20)
    precio = models.DecimalField(decimal_places = 2, max_digits = 10)
    sucursal = models.ForeignKey(Sucursal, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre

class Bebidas(models.Model):
    nombre = models.CharField(max_length = 30)
    tamaño = models.CharField(max_length = 30)
    proveedor = models.ForeignKey(Proveedor, on_delete = models.CASCADE)
    precio = models.DecimalField(decimal_places = 2, max_digits = 10)
    sucursal = models.ForeignKey(Sucursal, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre


class Combos(models.Model):
    nombre = models.CharField(max_length = 30)
    hamburguesas = models.ForeignKey(Hamburguesas, on_delete = models.CASCADE)
    bebida = models.ForeignKey(Bebidas, on_delete = models.CASCADE)
    Sucursal = models.ForeignKey(Sucursal,on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre
