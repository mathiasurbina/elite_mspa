from django import forms
from django.forms import ModelForm
from .models import Reserva, HorarioDisponible

HORAS_CHOICES = [
    ('09:00', '09:00'), ('10:00', '10:00'), ('11:00', '11:00'),
    ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'),
    ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'),
    ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'),
    ('21:00', '21:00'), ('22:00', '22:00')
]

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre', 'numero', 'email', 'fecha', 'hora']
        widgets = {
            'hora': forms.HiddenInput(),
        }

class HorarioDisponibleForm(forms.ModelForm):
    class Meta:
        model = HorarioDisponible
        fields = ['fecha', 'hora']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }


class HorariosMultiplesForm(forms.Form):
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    horas = forms.MultipleChoiceField(
        choices=HORAS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label="Selecciona las horas disponibles"
    )