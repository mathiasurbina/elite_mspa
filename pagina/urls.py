from django.urls import path
from .views import home, reserva, admin_panel, panel_reservas
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', home, name='home'),
    path('reserva/', reserva, name='reserva'),
    path('admin_panel/', admin_panel, name='admin_panel'),
    path('panel_reservas/', panel_reservas, name='panel_reservas'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('agregar-horarios/', views.agregar_horarios, name='agregar_horarios'),
    path('eliminar-horario/<int:horario_id>/', views.eliminar_horario, name='eliminar_horario'),
]
