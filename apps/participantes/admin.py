from django.contrib import admin

# Register your models here.
from apps.participantes.models import *


class PartidoPoliticoAdmmin(admin.ModelAdmin):
    list_display_links =listPartidos
    list_display =listPartidos
    ordering = ['lista']
admin.site.register(PartidosPoliticos,PartidoPoliticoAdmmin)


class JuntasInline(admin.StackedInline):
    extra = 2
    model = Juntas


class RecintosAdmin(admin.ModelAdmin):
    list_display_links = listRecintos
    list_display = listRecintos
    inlines = [JuntasInline]
admin.site.register(Recintos,RecintosAdmin)



class JuntasAdmin(admin.ModelAdmin):
    list_display_links = listJuntas
    list_display = listJuntas
admin.site.register(Juntas,JuntasAdmin)


class PersonasAdmin(admin.ModelAdmin):
    list_display = listConteoVotos
    list_display_links = listConteoVotos
admin.site.register(ConteoVotos,PersonasAdmin)


class CandidatosAdmin(admin.ModelAdmin):
    list_display_links = listCandidatos
    list_display = listCandidatos
admin.site.register(Candidatos,CandidatosAdmin)