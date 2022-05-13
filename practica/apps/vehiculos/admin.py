from logging import addLevelName
from django.contrib import admin
from apps.vehiculos.models import Vehiculo, TipoVehiculo, Marca
# Register your models here.

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'color', 'placa', 'motor', 'marca', 'tipovehiculo')
    ordering = ('modelo', 'color', 'placa', 'motor', 'marca', 'tipovehiculo')
    search_fields = ('modelo', 'marca__nombre', 'tipovehiculo__nombre')
    list_filter = ('modelo', 'color', 'placa', 'motor', 'marca', 'tipovehiculo')





admin.site.register(TipoVehiculo)
admin.site.register(Marca)
admin.site.register(Vehiculo, VehiculoAdmin)
