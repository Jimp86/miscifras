from django import template
from django.db.models import Sum
from apps.encuestas.models import IpPublica, VotosPresidente, VotosAlcalde, VotosConcejal
from apps.participantes.models import ConteoVotos

register = template.Library()

@register.simple_tag
def cuenta_por_candidato_junta(candidato_id,junta_id):
    try:
        votos=ConteoVotos.objects.filter(candidato_id=candidato_id,junta_id=junta_id).aggregate(Sum('numero_votos'))
        return votos['numero_votos__sum']
    except:
        return 0

@register.simple_tag
def cuenta_por_candidato_recinto(candidato_id,recinto_id):
    try:
        votos=ConteoVotos.objects.filter(candidato_id=candidato_id,junta__recinto_id=recinto_id).aggregate(Sum('numero_votos'))
        return votos['numero_votos__sum']
    except:
        return 0

@register.simple_tag
def cuenta_por_candidatos(candidato_id):
    try:
        votos=ConteoVotos.objects.filter(candidato_id=candidato_id).aggregate(Sum('numero_votos'))
        return votos['numero_votos__sum']
    except:
        return 0


@register.simple_tag
def cuenta_total_presidente():
    try:
        votos=VotosPresidente.objects.filter(candidato__dignidad="PRESIDENTE").aggregate(Sum('numero_votos'))
        return votos['numero_votos__sum']
    except:
        return 0


@register.simple_tag
def cuenta_total_alcalde():
    try:
        votos=VotosAlcalde.objects.filter(candidato__dignidad="ALCALDE").aggregate(Sum('numero_votos'))
        return votos['numero_votos__sum']
    except:
        return 0


@register.simple_tag
def cuenta_total_concejal():
    try:
        votos=VotosConcejal.objects.filter(candidato__dignidad="CONCEJAL").aggregate(Sum('numero_votos'))
        return votos['numero_votos__sum']
    except:
        return 0


@register.simple_tag
def cuenta_escanios(partido,divisor):
    try:
        votos=ConteoVotos.objects.filter(candidato__partido_id=partido,candidato__dignidad="CONCEJALES",candidato__consejalRural=False).aggregate(Sum('numero_votos'))
        return int((votos['numero_votos__sum'])/divisor)
    except:
        return 0


@register.simple_tag
def cuenta_escaniosRural(partido,divisor):
    try:
        votos=ConteoVotos.objects.filter(candidato__partido_id=partido,candidato__dignidad="CONCEJALES",candidato__consejalRural=True).aggregate(Sum('numero_votos'))
        return int((votos['numero_votos__sum'])/divisor)
    except:
        return 0

@register.simple_tag
def encuestaP(candidato_id):
    try:
        votos=VotosPresidente.objects.filter(candidato_id=candidato_id).aggregate(Sum('numero_votos'))
        return votos['numero_votos__sum']
    except:
        return 0


@register.simple_tag
def encuestaA(candidato_id):
    try:
        votos=VotosAlcalde.objects.filter(candidato_id=candidato_id).aggregate(Sum('numero_votos'))
        return votos['numero_votos__sum']
    except:
        return 0


@register.simple_tag
def encuestaC(candidato_id):
    try:
        votos=VotosConcejal.objects.filter(candidato_id=candidato_id).aggregate(Sum('numero_votos'))
        return votos['numero_votos__sum']
    except:
        return 0