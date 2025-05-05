from django.urls import path
from .views import home, reserva, admin_panel, panel_reservas

urlpatterns = [
    path('', home, name='home'),
    path('reserva/', reserva, name='reserva'),
    path('admin_panel/', admin_panel, name='admin_panel'),
    path('panel_reservas/', panel_reservas, name='panel_reservas'),
]
