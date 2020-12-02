from django.db import models
from alumnos.models import Alumno
from profesores.models import Profesor
# Create your models here.
class Clase(models.Model):
    materia=models.CharField(max_length=100)
    profesor=models.ManyToManyField(Profesor, related_name='profesor')
    horario=models.DateTimeField(null=True)

    alumno=models.ManyToManyField(Alumno, related_name='alumnos')

    def __str__(self):
        return self.materia