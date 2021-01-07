from ckeditor.fields import RichTextField
from django.db import models
import os
from django.utils.safestring import mark_safe

# Create your models here.

list_categoria = ['id', 'nombre']
class Categorias(models.Model):
    nombre = models.CharField(max_length=20, help_text="Máximo 20 Caracteres")

    def __str__(self):
        return self.nombre

list_etiqueta = ['id', 'categoria','nombre']
class Etiquetas(models.Model):
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20, help_text="Máximo 20 Caracteres")

    def __str__(self):
        return self.nombre

def generate_path(instance, filename):
    return os.path.join("img_noticias", "" + str(instance.tipo), filename)

list_archivo = ['id', 'fecha', 'tipo', 'formato', 'enlace']
class Archivos(models.Model):
    fecha = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    tipo = models.CharField(max_length=30, choices=(
    ("IMAGEN", "IMAGEN"), ("VIDEO", "VIDEO"), ("ENLACE", "ENLACE"), ("AUDIO", "AUDIO")), default="IMAGEN")
    formato = models.FileField(null=True, blank=True, upload_to=generate_path)
    enlace = models.CharField(max_length=500, null=True, blank=True)

app_noticias = ['id', 'categoria', 'destacada', 'titulo', 'detalles', 'visitas']
class Noticias(models.Model):
    fecha = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    etiqueta = models.ForeignKey(Etiquetas, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=120, help_text='Texto de no mas de 120 caracteres..!!', null=True, blank=True)
    portada = models.ImageField(upload_to='noticias/portada', null=True, blank=True)
    destacada = models.BooleanField(default=False)
    visitas = models.IntegerField(default=1)
    metadatos = models.TextField(null=True, blank=True)
    detalle = RichTextField(null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.titulo:
            self.titulo = str.upper(self.titulo)

        super(Noticias, self).save()

    def detalles(self):
        return mark_safe(self.detalle)