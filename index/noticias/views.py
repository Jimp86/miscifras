from django.shortcuts import render
from index.noticias.models import *

# Create your views here.

def noticias(request):
    notas = Noticias.objects.all().order_by('-fecha')
    contexto = {
        'noticias': notas,
        'destacadas': notas.filter(destacada=True).order_by('-fecha')[0:5],
        'populares': notas.order_by('-visitas'),
    }
    return render(request, "home/noticias.html", contexto)

def detnoticia(request,n):
    nota = Noticias.objects.get(id=n)
    nota.visitas +=1
    nota.save()
    notas = Noticias.objects.all()
    contexto={
        'noticia': Noticias.objects.get(id=n),
        'destacadas': notas.filter(destacada=True).order_by('-fecha')[0:5],
        'populares': notas.order_by('-visitas'),
    }
    return render(request, "home/det_noticias.html", contexto)