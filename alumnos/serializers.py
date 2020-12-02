from rest_framework import serializers
from alumnos.models import Alumno

class AlumnoSerializers(serializers.ModelSerializer):
    class Meta:
        model= Alumno
        fields= ('nombre', 'edad')