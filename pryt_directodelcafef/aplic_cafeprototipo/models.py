from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
