from django import forms
from django.forms import ModelForm
from .models import User, Reserva


class UserForm(forms.ModelForm):

    class Meta:
        model= User
        fields = ['usuario', 'email', 'clave', 'edad', 'pais']



class LoginForm(forms.Form):
    email = forms.EmailField(label='email')
    clave = forms.CharField(label='clave', widget=forms.PasswordInput)

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre', 'numero', 'email', 'fecha', 'hora']
        widgets = {
            'hora': forms.HiddenInput(),
        }
