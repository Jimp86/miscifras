from django.shortcuts import render
from index.noticias.models import *

# Create your views here.

def noticias(request):
    notas = Noticias.objects.all().order_by('-fecha')
    contexto = {
        'noticias': notas,
        'destacadas': notas.filter(destacada=True).order_by('-fecha')[0:4],
        'populares': notas.order_by('-visitas')[0:3],
    }
    return render(request, "home/noticias.html", contexto)

def noticia(request,n):
    nota = Noticias.objects.get(id=n)
    nota.visitas +=1
    nota.save()
    notas = Noticias.objects.all()
    contexto={
        'noticia': Noticias.objects.get(id=n),
        'destacadas': notas.filter(destacada=True).order_by('-fecha'),
        'populares': notas.order_by('-visitas'),
    }
    return render(request, "home/noticia.html", contexto)