from django.db import models
from django.utils import timezone


class Maestro(models.Model):
    class Cargo(models.TextChoices):
        MAESTRO = 'maestro', 'Maestro normal'
        DIRECTOR = 'director', 'Director'
        VICEDIRECTOR = 'vicedirector', 'Vicedirector'
        JEFE_DEPARTAMENTO = 'jefe_departamento', 'Jefe de departamento'

    nombre = models.CharField(max_length=100)
    cargo = models.CharField(
        max_length=20,
        choices=Cargo.choices,
        default=Cargo.MAESTRO,
    )
    fecha_incorporacion = models.DateField(default=timezone.localdate)

    class Meta:
        verbose_name = 'Maestro'
        verbose_name_plural = 'Maestros'
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} ({self.get_cargo_display()})"


class Alumno(models.Model):
    class Rol(models.TextChoices):
        ALUMNO = 'alumno', 'Alumno normal'
        DELEGADO = 'delegado', 'Delegado'
        SUBDELEGADO = 'subdelegado', 'Subdelegado'

    nombre = models.CharField(max_length=100)
    curso = models.CharField(max_length=50)
    rol = models.CharField(
        max_length=20,
        choices=Rol.choices,
        default=Rol.ALUMNO,
    )

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} - {self.curso}"


class Aula(models.Model):
    nombre = models.CharField(max_length=100)
    numero = models.PositiveIntegerField(unique=True)
    es_aula_huesped = models.BooleanField(
        choices=[
            (True, 'Aula huésped'),
            (False, 'No es aula huésped'),
        ],
        default=False,
    )

    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'
        ordering = ['numero']

    def __str__(self):
        return f"Aula {self.numero} - {self.nombre}"