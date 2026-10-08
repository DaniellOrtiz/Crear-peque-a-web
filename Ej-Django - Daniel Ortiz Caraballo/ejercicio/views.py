from django.http import HttpResponse


def index(request):
    return HttpResponse("¡Funciona! Esta es la página de inicio de ejercicio.")