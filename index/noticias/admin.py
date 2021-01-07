from django.contrib import admin

# Register your models here.
from index.noticias.models import *

class CategoriasAdmin(admin.ModelAdmin):
    list_display = list_categoria
    list_display_links = list_categoria
admin.site.register(Categorias, CategoriasAdmin)

class EtiquetasAdmin(admin.ModelAdmin):
    list_display = list_etiqueta
    list_display_links = list_etiqueta
admin.site.register(Etiquetas, EtiquetasAdmin)

class ArchivosAdmin(admin.ModelAdmin):
    list_display = list_archivo
    list_display_links = list_archivo
admin.site.register(Archivos, ArchivosAdmin)

class NoticiasAdmin(admin.ModelAdmin):
    list_display = app_noticias
    list_display_links = app_noticias
admin.site.register(Noticias, NoticiasAdmin)
