from django.shortcuts import render
from .models import *


def technology_week(request):
    palestrante = PalestranteInstrutor.objects.all()
    palestrantes = {'lista': palestrante}
    return render(request, 'blog/technology_week.html', palestrantes)
def technology_week(request):
    evento = Evento.objects.all()
    eventos = {'listaEventos':evento}
    return render(request, 'blog/technology_week.html', eventos)
