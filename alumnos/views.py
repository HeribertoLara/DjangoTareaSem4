from django.shortcuts import render
from django.http import HttpResponse
from alumnos.models import Alumno


# Create your views here.
def alumnos_views(request):
    response = ''
    alumnos=Alumno.objects.all()

    for alumno in alumnos:
        response += alumno.nombre

    return HttpResponse(response)

def get_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request,'alumnos/alumnos.html',{'alumnos':alumnos})


