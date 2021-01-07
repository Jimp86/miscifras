from django.db import models

# Create your models here.

from apps.participantes.models import Candidatos

listEncuesta = ['nombre','descripcion','titulo','notas']
class Encuesta(models.Model):
    #Categoria=
    #Etiqueta
    nombre=models.CharField(max_length=120,unique=True)
    imagen=models.ImageField(upload_to="Encuesta",null=True,blank=True)
    descripcion=models.TextField(max_length=300)
    titulo=models.CharField(max_length=120,unique=True)
    notas=models.TextField(max_length=300)

listIps = ['id','ip']
class IpPublica(models.Model):
    ip=models.CharField(max_length=35,null=True,blank=True)
    contador=models.IntegerField(default=5)

listPadron = ['id','cedula','nombres','provincia','canton','circunscripcion','parroquia','estadoParroquia','zona','junta','homonimo']
class PadronElectoral(models.Model):
    cedula=models.CharField(max_length=10,unique=True)
    nombres=models.CharField(max_length=120,null=True,blank=True)
    provincia=models.CharField(max_length=60,null=True,blank=True)
    canton=models.CharField(max_length=120,null=True,blank=True)
    circunscripcion=models.CharField(max_length=120,null=True,blank=True)
    parroquia=models.CharField(max_length=120,null=True,blank=True)
    estadoParroquia=models.CharField(max_length=120,null=True,blank=True)
    zona=models.CharField(max_length=120,null=True,blank=True)
    junta=models.CharField(max_length=120,null=True,blank=True)
    homonimo=models.CharField(max_length=120,null=True,blank=True)

listVotosPresidente = ['id', 'aceptado', 'fecha', 'cedula', 'candidato', 'numero_votos', 'ipPublica']
class VotosPresidente(models.Model):
    fecha=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    cedula=models.CharField(max_length=10,unique=True)
    candidato=models.ForeignKey(Candidatos,on_delete=models.CASCADE)
    numero_votos=models.IntegerField(default=0)
    ipPublica=models.CharField(max_length=35,default="")
    aceptado=models.BooleanField(default=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        ip = IpPublica.objects.last()
        self.ipPublica = ip.ip
        super(VotosPresidente, self).save()
        
listVotosAlcalde = ['id', 'aceptado', 'fecha', 'cedula', 'candidato', 'numero_votos', 'ipPublica']
class VotosAlcalde(models.Model):
    fecha=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    cedula=models.CharField(max_length=10,unique=True)
    candidato=models.ForeignKey(Candidatos,on_delete=models.CASCADE)
    numero_votos=models.IntegerField(default=0)
    ipPublica=models.CharField(max_length=35,default="")
    aceptado=models.BooleanField(default=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        ip = IpPublica.objects.last()
        self.ipPublica = ip.ip
        super(VotosAlcalde, self).save()

listVotosConcejal = ['id', 'aceptado', 'fecha', 'cedula', 'candidato', 'numero_votos', 'ipPublica']
class VotosConcejal(models.Model):
    fecha = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    cedula = models.CharField(max_length=10, unique=True)
    candidato = models.ForeignKey(Candidatos, on_delete=models.CASCADE)
    numero_votos = models.IntegerField(default=0)
    ipPublica = models.CharField(max_length=35, default="")
    aceptado=models.BooleanField(default=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        ip = IpPublica.objects.last()
        self.ipPublica = ip.ip
        print("registrado..!!")
        super(VotosConcejal, self).save()


