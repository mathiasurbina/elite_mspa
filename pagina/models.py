from django.db import models

# Create your models here.


class User(models.Model):
    usuario =models.CharField(max_length= 10, primary_key=True,verbose_name='Nombre Usuario')
    email = models.CharField(max_length=40, verbose_name='Email')
    clave = models.CharField(max_length=30, verbose_name='Clave')
    edad = models.CharField(max_length=3, verbose_name='Edad')
    pais = models.CharField(max_length=15, verbose_name='Pais')

    def __str__(self):
        return self.usuario
    
    

class Reserva(models.Model):
    nombre = models.CharField(max_length=100)
    numero = models.CharField(max_length=15)
    email = models.EmailField()
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"{self.nombre} - {self.fecha} a las {self.hora}"