import re
from urllib.request import urlopen
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from uuid import getnode as get_mac

from django.views.decorators.csrf import csrf_exempt
from apps.encuestas.models import IpPublica, VotosPresidente, VotosAlcalde, VotosConcejal
from apps.participantes.models import Candidatos
import math

def getPublicIp():
    data = str(urlopen('http://checkip.dyndns.com/').read())
    # data = '<html><head><title>Current IP Check</title></head><body>Current IP Address: 65.96.168.198</body></html>\r\n'
    ip = re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(data).group(1)
    print(data)
    print("Su IP Publica es: ", ip)
    return ip

def verificar_cedula(cedula=""):
    suma = 0
    ultimo_digito = 0
    if len(cedula) < 9:
        return False
    elif len(cedula) == 10:
        ultimo_digito = int(cedula[9])
        suma = 0
        cont = 2
        lista = list(cedula[0:9])
        print(lista)
        for i in lista:
            print(i, "*", cont, "=", int(i) * cont)
            valor = int(i) * cont
            if valor > 9:
                suma += valor - 9
            else:
                suma += valor
            if cont == 2:
                cont = 1
            else:
                cont = 2
    if (math.ceil((suma / 10)) * 10 - suma) == int(ultimo_digito):
        print((math.ceil((suma / 10)) * 10 - suma) == int(ultimo_digito))
        return True

    else:
        return False


@csrf_exempt
def registrarIP(request):
    if request.POST:
        ip = IpPublica(ip=request.POST['ip']).save()
        return HttpResponse("ok")
    else:
        pass


def obtenerVotosPresidente(request, n=0, cedula=""):
    ok = False
    print()
    if n == 0 and len(cedula) > 0:
        return HttpResponseRedirect('/encuestas/presidente')
    if len(cedula) == 10:
        ok = verificar_cedula(cedula)
    try:
        if ok:
            print('cédula correcta..!!')
            VotosPresidente(candidato_id=n, numero_votos=1, cedula=cedula).save()
            return HttpResponseRedirect('/encuestas/presidente')
    except Exception as error:
        print(error)
    contexto = {
        'participantes': Candidatos.objects.filter(dignidad="PRESIDENTE").order_by('partido__lista'),
        'totales': VotosPresidente.objects.filter(candidato__dignidad="PRESIDENTE")
    }
    return render(request, 'encuestas/presidente.html', contexto)


def obtenerVotosAlcalde(request, n=0, cedula=""):
    ok = False
    print()
    if n == 0 and len(cedula) > 0:
        return HttpResponseRedirect('/encuestas/alcalde')
    if len(cedula) == 10:
        ok = verificar_cedula(cedula)
    try:
        if ok:
            print('cedula correcta..!!')
            VotosAlcalde(candidato_id=n, numero_votos=1, cedula=cedula).save()
            return HttpResponseRedirect('/encuestas/alcalde')
    except Exception as error:
        print(error)
    contexto = {
        'participantes': Candidatos.objects.filter(dignidad="ALCALDE").order_by('partido__lista'),
        'totales': VotosAlcalde.objects.filter(candidato__dignidad="ALCALDE")
    }
    return render(request,'encuestas/alcalde.html',contexto)


def obtenerVotosConcejal(request, n=0, cedula=""):
    ok = False
    if n == 0 and len(cedula) > 0:
        return HttpResponseRedirect('/encuestas/concejal/')
    if len(cedula) == 10:
        ok = verificar_cedula(cedula)
    try:
        if ok:
            print('cedula correcta..!!')
            VotosConcejal(candidato_id=n, numero_votos=1, cedula=cedula).save()
            print('registrado..!!')
            return HttpResponseRedirect('/encuestas/concejal/')
    except Exception as error:
        print(error)
    contexto = {
        'participantes': Candidatos.objects.filter(dignidad="CONCEJALES").order_by('partido__lista'),
        'totales': VotosConcejal.objects.filter(candidato__dignidad="CONCEJALES"),
    }
    return render(request, 'encuestas/concejal.html', contexto)
