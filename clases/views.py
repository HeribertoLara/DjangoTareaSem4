from django.shortcuts import render
from django.http import HttpResponse
from clases.models import Clase


# Create your views here.
def clases_views(request):
    response = ''
    clases= Clase.objects.all()

    for clase in clases:
        response += clase.materia

    return HttpResponse(response)

def get_clases(request):
    clases = Clase.objects.all()
    return render(request,'clases/clases.html',{'clases':clases})

def get_clase(request,clase_id):
    clase=Clase.objects.get(id=clase_id)
    return render(request, 'clases/clase_id.html',{'clase':clase})