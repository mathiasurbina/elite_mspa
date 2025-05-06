from django.db import models

# Create your models here.



    
class Reserva(models.Model):
    nombre = models.CharField(max_length=100)
    numero = models.CharField(max_length=15)
    email = models.EmailField()
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"{self.nombre} - {self.fecha} a las {self.hora}"
    
class HorarioDisponible(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"{self.fecha} - {self.hora}"