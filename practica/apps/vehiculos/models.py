from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

class TipoVehiculo(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre

class Vehiculo(models.Model):
    modelo = models.CharField(max_length=30)
    color = models.CharField(max_length=20)
    placa = models.CharField(max_length=15)
    motor = models.CharField(max_length=10)
    marca = models.ForeignKey(Marca, null=True, blank=True, on_delete=models.CASCADE)
    tipovehiculo = models.ForeignKey(TipoVehiculo, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Tipo de Vehiculos")

    def __str__(self):
        return self.modelo

