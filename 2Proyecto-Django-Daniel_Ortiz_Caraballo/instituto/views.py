from django.shortcuts import render

from .models import Alumno, Aula, Maestro


def maestro_list(request):
    maestros = Maestro.objects.all()
    return render(request, 'instituto/maestro_list.html', {'maestros': maestros})


def alumno_list(request):
    alumnos = Alumno.objects.all()
    return render(request, 'instituto/alumno_list.html', {'alumnos': alumnos})


def aula_list(request):
    aulas = Aula.objects.all()
    return render(request, 'instituto/aula_list.html', {'aulas': aulas})