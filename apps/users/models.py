from django.contrib.auth.models import User
from django.db import models


class Pais(models.Model):
    pais = models.CharField(max_length=120)

    def __str__(self):
        return self.pais

class Provincia(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    provincia = models.CharField(max_length=120)

    def __str__(self):
        return self.provincia

class Canton(models.Model):
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    canton = models.CharField(max_length=120)

    def __str__(self):
        return self.canton

class Parroquia(models.Model):
    canton = models.ForeignKey(Canton, on_delete=models.CASCADE)
    parroquia = models.CharField(max_length=120)

    def __str__(self):
        return self.parroquia

#app_perfil=['cedula','email','nombre','apellido','sexo','fecha_nacimiento','provincia','canton','parroquia','active','staff','admin']
class Usuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    cedula = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=50, null=True, blank=True, unique=True)
    nombre = models.CharField(max_length=50, null=True, blank=True)
    apellido = models.CharField(max_length=50, null=True, blank=True)
    sexo = models.CharField(max_length=10, choices=(("MASCULINO", "MASCULINO"), ("FEMENINO", "FEMENINO")))
    fecha_nacimiento = models.DateTimeField(null=True, blank=True)
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE)
    celular = models.CharField(max_length=10, null=True, blank=True, unique=True)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"