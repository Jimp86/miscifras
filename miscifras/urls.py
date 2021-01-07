"""miscifras URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from index.noticias.views import *
from index.home.views import *
#from index.nosotros.views import *
from apps.encuestas.views import obtenerVotosPresidente, obtenerVotosAlcalde, obtenerVotosConcejal, registrarIP
from apps.users.views import registro, login_usuario, logout_usuario, perfiles
from apps.participantes.views import *

urlpatterns = [
    #django
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    #Home&register
    path('', Home, name="home"),
    path('noticias/', noticias, name="noticias"),
    path("noticia/<int:n>/", detnoticia, name="detnoticia"),
    #path('nosotros/', nosotros, name="nosotros"),
    #Login&register
    path('log_in/', login_usuario),
    path('log_out/', logout_usuario),
    path('registro/', registro),
    path('perfil/', perfiles),

    #Apps
    #path('encuestas', encuestas, name="encuestas"),

    #Encuesta
    path('control/',seleccionarJunta),
    path('candidatos/<int:junta>/',seleccionarDignidad),
    path('njunta/<int:recinto>/<slug:genero>/',obtenerNumerosJunta),
    path('alcaldes/<int:junta>/',alcalde),
    path('prefectos/<int:junta>/',prefecto),
    path('concejales/Urbanos/<int:junta>/',concejalesUrbano),
    path('concejales/Rural/<int:junta>/',concejalesRural),
    #alcaldes:
    path('rjunta/<int:junta>/',resultadosJunta),
    path('rRecinto/<int:recinto>/',resultadosRecinto),
    path('rtodoAlcaldes/', resultadosTodo),
    #prefectos:
    path('rjuntaPre/<int:junta>/',resultadosJuntaPrefecto),
    path('rRecintoPre/<int:recinto>/',resultadosRecintoPrefecto),
    path('rtodoPrefecto/', resultadosTodoPrefecto),
    #concejales
    path('rconcejales/<slug:n>/', resultadosConcejales),
    path('tconcejales/<slug:n>/', tablaDatosConcejales),
    path('encuestas/presidente/',obtenerVotosPresidente),
    path('encuestas/presidente/<int:n>/<slug:cedula>/',obtenerVotosPresidente),
    path('encuestas/alcalde/',obtenerVotosAlcalde),
    path('encuestas/alcalde/<int:n>/<slug:cedula>/',obtenerVotosAlcalde),
    path('encuestas/concejal/',obtenerVotosConcejal),
    path('encuestas/concejal/<int:n>/<slug:cedula>/',obtenerVotosConcejal),
    path('regip/',registrarIP),
 ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Administración Mis Cifras"