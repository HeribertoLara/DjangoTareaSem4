from django.shortcuts import render
from django.http import HttpResponse
from profesores.models import Profesor

def get_profesores(request):
    profesores = Profesor.objects.all()
    return render(request,'profesores.html',{'profesores':profesores})

def get_profesor(request,profesor_id):
    profesor_id=Profesor.objects.get(id=profesor_id)
    return render(request, 'profesor_id.html',{'profesor':profesor_id})