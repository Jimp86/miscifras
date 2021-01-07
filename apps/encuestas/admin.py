from django.contrib import admin

# Register your models here.
#from apps.encuestas.models import listVotosPresidente, listVotosAlcalde, listVotosConcejal, VotosPresidente, VotosAlcalde, VotosConcejal, listIps, IpPublica, listPadron, PadronElectoral, Encuesta
from apps.encuestas.models import *

class EncuestaAdmin(admin.ModelAdmin):
    list_display_links = listEncuesta
    list_display = listEncuesta
admin.site.register(Encuesta,EncuestaAdmin)


class IpsAdmin(admin.ModelAdmin):
    list_display_links = listIps
    list_display = listIps
admin.site.register(IpPublica,IpsAdmin)


class VotosAdminP(admin.ModelAdmin):
    list_display = listVotosPresidente
    list_display_links = listVotosPresidente
    search_fields = ['cedula']
admin.site.register(VotosPresidente,VotosAdminP)


class VotosAdminA(admin.ModelAdmin):
    list_display = listVotosAlcalde
    list_display_links = listVotosAlcalde
    search_fields = ['cedula']
admin.site.register(VotosAlcalde,VotosAdminA)

class VotosAdminC(admin.ModelAdmin):
    list_display = listVotosConcejal
    list_display_links = listVotosConcejal
    search_fields = ['cedula']
admin.site.register(VotosConcejal,VotosAdminC)


class PadronAdmin(admin.ModelAdmin):
    list_display = listPadron
    list_display_links = listPadron
    search_fields = ['nombres']
admin.site.register(PadronElectoral,PadronAdmin)