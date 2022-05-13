from django.db import models
from django.contrib.auth.models import User 
from apps.vehiculos.models import Vehiculo

# Create your models here.

class Venta(models.Model):
    fecha = models.DateField()
    valortotal = models.BigIntegerField()
    tipopago = models.CharField(max_length=20)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    vehiculo = models.ManyToManyField(Vehiculo, through='VehiculoVenta')

    def __str__(self):
        return self.tipopago

class VehiculoVenta(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, null=False, blank=False, on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta, null=False, blank=False, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.BigIntegerField()