from django.db import models

# Create your models here.

listPartidos=['id','nombre','lista','logo']
class PartidosPoliticos(models.Model):
    nombre=models.CharField(max_length=60)
    lista=models.IntegerField(default=0)
    logo=models.ImageField(upload_to='logos',null=True,blank=True)

    def __str__(self):
        return "%s [%s]"%(self.nombre,self.lista)
    
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.nombre=str.upper(self.nombre)
        
        super(PartidosPoliticos, self).save()

listRecintos=['id','nombre']
class Recintos(models.Model):
    nombre=models.CharField(max_length=50,)

    def __str__(self):

        return self.nombre

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.nombre=str.upper(self.nombre)

        super(Recintos, self).save()


listJuntas=['recinto','genero','numero']
class Juntas(models.Model):
    recinto=models.ForeignKey(Recintos,on_delete=models.CASCADE)
    genero=models.CharField(max_length=60, choices=(("MASCULINO","MASCULINO"),("FEMENINO","FEMENINO")))
    numero=models.CharField(max_length=20)

    def __str__(self):
        if self.genero=="MASCULINO":
            return "%s - %s [%s]"%("M",self.numero,self.recinto.nombre)
        else:
            return "%s - %s [%s]"%("F", self.numero,self.recinto.nombre)


listCandidatos=['id','partido','dignidad','nombre']
class Candidatos(models.Model):
    partido = models.ForeignKey(PartidosPoliticos, on_delete=models.CASCADE)
    dignidad = models.CharField(choices=(("ASAMBLEISTA", "ASAMBLEISTA"), ("PRESIDENTE", "PRESIDENTE"), ("ALCALDE", "ALCALDE"), ("PREFECTO", "PREFECTO"), ("CONCEJALES", "CONCEJALES")), max_length=30)
    nombre = models.CharField(max_length=60)
    foto=models.ImageField(upload_to='encuesta',null=True,blank=True)
    consejalRural=models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.nombre=str.upper(self.nombre)

        super(Candidatos, self).save()


listConteoVotos=['id','candidato','dignidad','junta','numero_votos']
class ConteoVotos(models.Model):
    candidato=models.ForeignKey(Candidatos,on_delete=models.CASCADE,null=True,blank=True)
    junta=models.ForeignKey(Juntas,on_delete=models.CASCADE)
    numero_votos=models.IntegerField(default=0)


    def dignidad(self):
        return self.candidato.dignidad

    
    


