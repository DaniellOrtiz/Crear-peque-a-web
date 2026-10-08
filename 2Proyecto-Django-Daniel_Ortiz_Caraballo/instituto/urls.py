from django.urls import path

from . import views

app_name = 'instituto'

urlpatterns = [
    path('maestros/', views.maestro_list, name='maestro_list'),
    path('alumnos/', views.alumno_list, name='alumno_list'),
    path('aulas/', views.aula_list, name='aula_list'),
]