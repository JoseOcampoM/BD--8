from django.shortcuts import render, redirect
from apps.vehiculos.formVehiculo import VehiculoForm
from apps.vehiculos.models import Vehiculo
# Create your views here.

def listVehiculos(request):
    vehiculos = Vehiculo.objects.all().order_by('-id')
    context = {'vehiculos': vehiculos}
    return render(request, 'vehiculos/listVehiculos.html', context)

def home(request):
    return render(request, 'base/base.html')

def vehiculoCreate(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('vehiculos:listVehiculos')
    else:
        form=VehiculoForm()
    return render(request, 'vehiculos/vehiculo_form.html', {'form':form})