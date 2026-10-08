from django.contrib import admin

from .models import Alumno, Aula, Maestro

admin.site.register(Maestro)
admin.site.register(Alumno)
admin.site.register(Aula)