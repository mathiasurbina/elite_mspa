from django.contrib import admin
from .models import Reserva

# Register your models here.

from .models import User
admin.site.register(User)
admin.site.register(Reserva)
