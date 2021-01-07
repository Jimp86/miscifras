from django.shortcuts import render
from index.noticias.models import *

# Create your views here.

def Home(request):
    contexto = {
        #'noticias': noticias.objects.filter(muy_relevante=True).order_by('-fecha'),
        #'notas': noticias.objects.filter(poco_relevante=True).order_by('-fecha'),

        'recientes': Noticias.objects.all().order_by('-fecha')[0:8],
        'destacadas': Noticias.objects.filter(destacada=True).order_by('-fecha')[0:5],
        'populares': Noticias.objects.all().order_by('-visitas')[0:5],
        'noticiasSplash': Noticias.objects.all().order_by('-fecha'),
    }
    return render(request, "home/home.html", contexto)