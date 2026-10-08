from django.conf import settings
from django.db import models
from django.utils import timezone


class Animal(models.Model):
    cuidador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='animales',
    )
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animales'

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"


class Protectora(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Protectora'
        verbose_name_plural = 'Protectoras'

    def __str__(self):
        return self.nombre


class Colaborador(models.Model):
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    fecha_entrada_protectora = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'

    def __str__(self):
        return f"{self.nombre} - {self.cargo}"