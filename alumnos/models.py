from django.db import models
#from clases.models import Clase

# Create your models here.
class Alumno(models.Model):
    nombre=models.CharField(max_length=200)
    edad=models.IntegerField(null=True)

    def __str__(self):
        return self.nombre

