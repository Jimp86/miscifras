from django.db import models

# Create your models here.

list_presentacion = ['titulo', 'subtitulo', 'descripcion']
class Presentacion(models.Model):
    titulo=models.CharField(max_length=50, null=True, blank=True)
    imagen=models.ImageField(upload_to="presentacion")
    subtitulo=models.CharField(max_length=100, null=True, blank=True)
    descripcion=models.TextField(max_length=300)

    class Meta:
        verbose_name_plural="1.2 Presentación"

list_nosotros = ['titulo', 'descripcion']
class Nosotros(models.Model):
    titulo=models.CharField(max_length=100,null=True,blank=True)
    icono=models.CharField(max_length=30,null=True,blank=True)
    descripcion=models.TextField(max_length=200,null=True,blank=True)

    class Meta:
        verbose_name_plural="1.3 Nosotros"
