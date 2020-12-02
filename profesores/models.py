from django.db import models
# Create your models here.
class Profesor(models.Model):
    nombre = models.CharField(max_length=200)
    materia = models.CharField(max_length=20)
    correo = models.CharField(max_length=50)
    edad = models.IntegerField(null=True)

    def __str__(self):
        return self.nombre