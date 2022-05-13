from django.urls import path
from apps.vehiculos.views import listVehiculos, vehiculoCreate

app_name='vehiculos'
urlpatterns = [
    path('', listVehiculos, name= 'listVehiculos'),
    path('nuevo/', vehiculoCreate, name= 'vehiculoCreate'),
]