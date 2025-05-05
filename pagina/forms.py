from django import forms
from django.forms import ModelForm
from .models import Reserva



class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre', 'numero', 'email', 'fecha', 'hora']
        widgets = {
            'hora': forms.HiddenInput(),
        }
