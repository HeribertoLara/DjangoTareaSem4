from django.db import models
from alumnos.models import Alumno
# Create your models here.
class Clase(models.Model):
    materia=models.CharField(max_length=100)
    profesor=models.CharField(max_length=100)
    horario=models.DateTimeField(null=True)

    alumno=models.ManyToManyField(Alumno, related_name='alumnos')

    def __str__(self):
        return self.materia