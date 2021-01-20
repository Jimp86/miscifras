from django.shortcuts import render
from index.noticias.models import *

# Create your views here.

def Home(request):
    contexto = {
        'recientes': Noticias.objects.all().order_by('-fecha')[0:5],
        'destacadas': Noticias.objects.filter(destacada=True).order_by('-fecha')[0:6],
        'populares': Noticias.objects.all().order_by('-visitas')[0:6],
        'noticiasSplash': Noticias.objects.all().order_by('-fecha'),
    }
    return render(request, "home/home.html", contexto)