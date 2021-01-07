from django.contrib import admin

# Register your models here.
from index.home.models import *

class PresentacionAdmin(admin.ModelAdmin):
    list_display = list_presentacion
    list_display_links = list_presentacion
admin.site.register(Presentacion, PresentacionAdmin)

class NosotrosAdmin(admin.ModelAdmin):
    list_display = list_nosotros
    list_display_links = list_nosotros
admin.site.register(Nosotros, NosotrosAdmin)