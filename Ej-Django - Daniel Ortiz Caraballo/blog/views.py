from django.shortcuts import render

from .models import Animal, Colaborador, Protectora


def animal_list(request):
    animales = Animal.objects.select_related('cuidador').all()
    return render(request, 'blog/animal_list.html', {'animales': animales})


def protectora_list(request):
    protectoras = Protectora.objects.all()
    return render(request, 'blog/protectora_list.html', {'protectoras': protectoras})


def colaborador_list(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'blog/colaborador_list.html', {'colaboradores': colaboradores})