from django.shortcuts import render
from .models import  Reserva
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import  ReservaForm
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'pagina/home.html')


def reserva(request):
    horas_totales = ["10:00", "11:00", "12:00", "15:00", "16:00"]

   
    if request.method == 'GET' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        fecha = request.GET.get('fecha')
        reservas = Reserva.objects.filter(fecha=fecha)
        horas_ocupadas = [r.hora.strftime('%H:%M') for r in reservas]
        horas_disponibles = [h for h in horas_totales if h not in horas_ocupadas]
        return JsonResponse({'horas': horas_disponibles})


    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'pagina/reserva_confirmada.html', {'reserva': form.instance})
    else:
        form = ReservaForm()

    return render(request, 'pagina/reserva.html', {'form': form})

def carrito(request):
    return render(request, 'pagina/carrito.html')

def olvido(request):
    return render(request, 'pagina/olvido.html')



@login_required
def admin_panel(request):
    reservas = Reserva.objects.all().order_by('-fecha', 'hora')
    return render(request, 'pagina/admin_panel.html', {'reservas': reservas})    

@login_required
def panel_reservas(request):
    reservas = Reserva.objects.all().order_by('fecha', 'hora')
    return render(request, 'pagina/panel_reservas.html', {'reservas': reservas})