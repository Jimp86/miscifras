from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from apps.participantes.models import Candidatos, Juntas, Recintos, ConteoVotos, PartidosPoliticos


def seleccionarDignidad(request,junta):
    contexto={
        'junta':Juntas.objects.get(id=junta),
    }
    return render(request,'seleccionar.html',contexto)


def obtenerNumerosJunta(request,recinto,genero):
    juntas=Juntas.objects.filter(recinto_id=recinto, genero=genero)

    opciones=''
    for junta in juntas:
        opciones+="""<option value='%s'>%s</option>"""%(junta.id,junta.numero)

    print(opciones)
    return HttpResponse(opciones)


def seleccionarJunta(request):
    contexto={
        'recintos':Recintos.objects.all(),
        'juntas':Juntas.objects.all(),
        'user':request.user,
    }
    return render(request,'seleccionarJunta.html',contexto)




def alcalde(request,junta):
    juntas=Juntas.objects.get(id=junta)
    mensaje=""
    if request.POST:
        print(request.POST)
        for i in request.POST:
            if i!='csrfmiddlewaretoken':
                try:
                    VALOR=ConteoVotos.objects.get(candidato_id=i,junta_id=junta)
                    mensaje="NO ES POSIBLE INGRESAR DOS VECES"
                except Exception as error:
                    print(error)
                    conteo=ConteoVotos(candidato_id=i,junta_id=junta,numero_votos=request.POST[i])
                    conteo.save()
                    mensaje="SE HA REGISTRADO TODOS LOS DATOS..!!"
        return render(request, 'seleccionar.html', {'junta':juntas,'mensaje':mensaje})
    contexto = {
        'junta': Juntas.objects.get(id=junta),
        'participantes': Candidatos.objects.filter(dignidad="ALCALDE").order_by('partido__lista'),
        'mensaje':mensaje,
    }
    return render(request,'alcaldes.html',contexto)

def prefecto(request,junta):
    juntas = Juntas.objects.get(id=junta)
    mensaje = ""
    if request.POST:
        print(request.POST)
        for i in request.POST:
            if i != 'csrfmiddlewaretoken':
                try:
                    VALOR=ConteoVotos.objects.get(candidato_id=i,junta_id=junta)
                    mensaje="NO ES  POSIBLE INGRESAR DOS VECES"
                except Exception as error:
                    print(error)
                    conteo=ConteoVotos(candidato_id=i,junta_id=junta,numero_votos=request.POST[i])
                    conteo.save()
                    mensaje="SE HA REGISTRADO TODOS LOS DATOS..!!"
        return render(request, 'seleccionar.html', {'junta':juntas,'mensaje':mensaje})

    contexto = {
        'junta': Juntas.objects.get(id=junta),
        'participantes': Candidatos.objects.filter(dignidad="PREFECTO").order_by('partido__lista')
    }
    return render(request,'prefectos.html',contexto)


def concejalesUrbano(request,junta):
    juntas = Juntas.objects.get(id=junta)
    mensaje = ""
    if request.POST:
        print(request.POST)
        for i in request.POST:
            if i != 'csrfmiddlewaretoken':
                try:
                    VALOR=ConteoVotos.objects.get(candidato_id=i,junta_id=junta)
                    mensaje="NO ES  POSIBLE INGRESAR DOS VECES"
                except Exception as error:
                    print(error)
                    conteo=ConteoVotos(candidato_id=i,junta_id=junta,numero_votos=request.POST[i])
                    conteo.save()
                    mensaje="SE HA REGISTRADO TODOS LOS DATOS..!!"
        return render(request, 'seleccionar.html', {'junta':juntas,'mensaje':mensaje})

    contexto = {
        'junta': Juntas.objects.get(id=junta),
        'participantes': Candidatos.objects.filter(dignidad="CONCEJALES",consejalRural=False).order_by('partido'),
        'partidos':PartidosPoliticos.objects.filter(concejal=True).order_by('lista'),
    }
    return render(request,'concejales.html',contexto)

def concejalesRural(request,junta):
    juntas = Juntas.objects.get(id=junta)
    mensaje = ""
    if request.POST:
        print(request.POST)
        for i in request.POST:
            if i != 'csrfmiddlewaretoken':
                try:
                    VALOR=ConteoVotos.objects.get(candidato_id=i,junta_id=junta)
                    mensaje="NO ES  POSIBLE INGRESAR DOS VECES"
                except Exception as error:
                    print(error)
                    conteo=ConteoVotos(candidato_id=i,junta_id=junta,numero_votos=request.POST[i])
                    conteo.save()
                    mensaje="SE HA REGISTRADO TODOS LOS DATOS..!!"
        return render(request, 'seleccionar.html', {'junta':juntas,'mensaje':mensaje})

    contexto = {
        'junta': Juntas.objects.get(id=junta),
        'participantes': Candidatos.objects.filter(dignidad="CONCEJALES",consejalRural=True).order_by('partido'),
        'partidos':PartidosPoliticos.objects.filter(concejal=True).order_by('lista'),
    }
    return render(request,'concejalesRural.html',contexto)

#resultados de alcalde
def resultadosJunta(request,junta=0):
    juntas=None
    if junta>0:
        juntas=Juntas.objects.get(id=junta)
    contexto={
        'junta':juntas,
        'alcaldes':Candidatos.objects.filter(dignidad='ALCALDE'),
        'juntas':Juntas.objects.all(),
    }
    return render(request,'resultadosJunta.html',contexto)


def resultadosRecinto(request,recinto=0):
    recintos=None
    if recinto>0:
        recintos=Recintos.objects.get(id=recinto)
    contexto={
        'recinto':recintos,
        'alcaldes':Candidatos.objects.filter(dignidad='ALCALDE'),
        'recintos':Recintos.objects.all(),
    }
    return render(request,'resultadosRecintos.html',contexto)


def resultadosTodo(request):
    contexto={
        'alcaldes':Candidatos.objects.filter(dignidad='ALCALDE'),
    }
    return render(request,'resultadosCandidatos.html',contexto)


#resultados prefectos
def resultadosJuntaPrefecto(request,junta=0):
    juntas=None
    if junta>0:
        juntas=Juntas.objects.get(id=junta)
    contexto={
        'junta':juntas,
        'alcaldes':Candidatos.objects.filter(dignidad='PREFECTO'),
        'juntas':Juntas.objects.all(),
    }
    return render(request,'resultadosJuntaPrefectos.html',contexto)


def resultadosRecintoPrefecto(request,recinto=0):
    recintos=None
    if recinto>0:
        recintos=Recintos.objects.get(id=recinto)
    contexto={
        'recinto':recintos,
        'alcaldes':Candidatos.objects.filter(dignidad='PREFECTO'),
        'recintos':Recintos.objects.all(),
    }
    return render(request,'resultadosRecintosPre.html',contexto)


def resultadosTodoPrefecto(request):
    contexto={
        'alcaldes':Candidatos.objects.filter(dignidad='PREFECTO'),
    }
    return render(request,'resultadosCandidatoPrefecto.html',contexto)

def resultadosConcejales(request,n):
    participantes = None
    if n == "R":
        participantes = Candidatos.objects.filter(dignidad='CONCEJALES', consejalRural=True).order_by("partido")
    elif n == 'U':
        participantes = Candidatos.objects.filter(dignidad='CONCEJALES',consejalRural=False).order_by("partido")
    contexto={
        'alcaldes':participantes,
        'n':n,
    }
    return render(request,'resultadosConcejales.html',contexto)


def tablaDatosConcejales(request,n):
    participantes=None
    if n=="R":
        participantes=Candidatos.objects.filter(dignidad='CONCEJALES',consejalRural=True).order_by("partido")
    elif n=="U":
        participantes = Candidatos.objects.filter(dignidad='CONCEJALES',consejalRural=False).order_by("partido")
    contexto={
        'participantes':participantes,
        'partidos':PartidosPoliticos.objects.filter(concejal=True).order_by('lista'),
        'n':n,
    }
    return render(request,'TablaConcejales.html',contexto)