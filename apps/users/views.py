from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from .models import Pais, Provincia, Canton, Parroquia, Usuario

# Listas
def returnProvincias(request, id):
    return render(request, "snipers/provincia.html", {"provincias": Provincia.objects.filter(pais_id=id)})

def returnCantones(request, id):
    return render(request, "snipers/ciudad.html", {"cantones": Canton.objects.filter(provincia_id=id)})

def returnParroquias(request, id):
    return render(request, "snipers/ciudad.html", {"parroquias": Parroquia.objects.filter(canton_id=id)})

def registro(request):
    mensaje = ""
    if request.POST:
        user = User.objects.create_user(username=request.POST["email"], password=request.POST["password2"],
                                        email=request.POST["email"], is_active=True)
        user.save()
        # if email_aws_smtp(user.email, "verificación de Email",
        #                   "Gracias por registrarte en nuestra aplicación, para verificar tu direccion por favor da clic sobre el siguiente enlace: <a href='http://tripbuss.com/auth/user/" + str(
        #                           user.id) + "'>CLick Aqui para ctivar la cuenta</a>"):
        #     mensaje = "Tu registro se ha creado exitosamente, sin embargo es necesario que verifiques tú dirección de email"
        # else:
        #     mensaje = "Tu registro se ha creado exitosamente, sin embargo es necesario que verifiques tú dirección de email"
    contexto={
        #"global": Global.objects.last(),
        #"ciudades":Ciudad.objects.all().order_by("?").order_by("provincia_id").order_by("nombre")[:70][::-1],
    }
    return render(request,"registro/registro.html",contexto)

def login_usuario(request):
    mensaje=""
    if request.POST:
        email = request.POST["email"]
        password = request.POST['password']
        user = None
        try:
            user = User.objects.get(email=email)
            if user.is_active:
                user = auth.authenticate(username=user.username, password=password)
        except:
            mensaje="No existe el usuario ingresado"
        if user and user.is_active:
            auth.login(request, user=user)
            return HttpResponseRedirect("/")
        else:
            mensaje = "El Usuario no ha verificado su cuenta de email."
    contexto={
        #"mensaje":mensaje,
        #"global": Global.objects.last(),
        #"ciudades":Ciudad.objects.all().order_by("?").order_by("provincia_id").order_by("nombre")[:70][::-1],
    }
    return render(request, "registro/login.html",contexto)

@login_required(login_url="/log_in/")
def logout_usuario(request):
    auth.logout(request)
    return render(request, "home/home.html")

# Email
def verificacion_email(request):
    try:
        user = User.objects.get(email=request.GET["email"])
        return HttpResponse(True)
    except:
        return HttpResponse(False)

@login_required(login_url="/log_in/")
def perfiles(request):
    mensaje = ""
    perfil = None
    try:
        perfil = Usuario.objects.get(usuario=request.user)
    except:
        pass
    if request.POST:
        try:
            perfil = Usuario.objects.get(usuario=request.user)
            perfil.usuario = request.user
            perfil.email = request.user.email
            perfil.cedula = request.POST["cedula"]
            perfil.nombres = request.POST["nombres"]
            perfil.apellidos = request.POST["apellidos"]
            perfil.sexo = request.POST["sexo"]
            perfil.fecha_nacimiento = request.POST["fecha_nacimiento"]
            perfil.celular = request.POST["celular"]
            if "parroquia_id" in request.POST:
                perfil.parroquia_id = request.POST["parroquia_id"]
            perfil.save()
            mensaje = "Los datos fueron actualizados."
        except:
            if "parroquia_id" in request.POST:
                perfil = Usuario(usuario=request.user, email=request.user.email, nombres=request.POST["nombres"],
                                        apellidos=request.POST["apellidos"],
                                        cedula=request.POST["cedula"], celular=request.POST["celular"],
                                        parroquia_id=request.POST["parroquia_id"])
                perfil.save()
            else:
                perfil = Usuario(usuario=request.user, email=request.user.email, nombres=request.POST["nombres"],
                                        apellidos=request.POST["apellidos"],
                                        cedula=request.POST["cedula"], celular=request.POST["celular"])
                perfil.save()
            mensaje = "Los datos fueron creados exitosamente."

    contexto = {
        "perfil": perfil,
        "paises": Pais.objects.all(),
        "mensaje": mensaje,
        # "global": Global.objects.last(),
    }
    return render(request, "registro/perfil.html", contexto)