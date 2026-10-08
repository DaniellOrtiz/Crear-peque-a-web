from django.contrib import admin

from .models import Animal, Colaborador, Protectora

admin.site.register(Animal)
admin.site.register(Protectora)
admin.site.register(Colaborador)