from django.shortcuts import render
from .models import  Reserva, HorarioDisponible
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import  ReservaForm, HorarioDisponibleForm, HorariosMultiplesForm
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q



def home(request):
    return render(request, 'pagina/home.html')


def reserva(request):
    if request.method == 'GET' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        fecha = request.GET.get('fecha')
        
        
        horarios = HorarioDisponible.objects.filter(fecha=fecha)
        
        
        reservas = Reserva.objects.filter(fecha=fecha)
        horas_tomadas = [r.hora.strftime('%H:%M') for r in reservas]
        
        
        horas_disponibles = [h.hora.strftime('%H:%M') for h in horarios if h.hora.strftime('%H:%M') not in horas_tomadas]

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

    horas_ocupadas = Reserva.objects.values_list('fecha', 'hora')
    filtro = Q()

    for fecha, hora in horas_ocupadas:
        filtro |= Q(fecha=fecha, hora=hora)

    disponibles = HorarioDisponible.objects.exclude(filtro).order_by('fecha', 'hora')

    return render(request, 'pagina/panel_reservas.html', {
        'reservas': reservas,
        'disponibles': disponibles
    })

def agregar_horarios(request):
    if request.method == 'POST':
        form = HorariosMultiplesForm(request.POST)
        if form.is_valid():
            fecha = form.cleaned_data['fecha']
            horas = form.cleaned_data['horas']
            for hora in horas:
                HorarioDisponible.objects.create(fecha=fecha, hora=hora)
            return redirect('agregar_horarios')
    else:
        form = HorariosMultiplesForm()
    
    return render(request, 'pagina/agregar_horarios.html', {'form': form})

@login_required
def eliminar_horario(request, horario_id):
    if request.method == 'POST':
        horario = get_object_or_404(HorarioDisponible, id=horario_id)
        horario.delete()
    return redirect('panel_reservas')

def eliminar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    reserva.delete()
    return redirect('panel_reservas') 