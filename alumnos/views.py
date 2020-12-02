from django.shortcuts import render
from django.http import HttpResponse
from alumnos.models import Alumno
from alumnos.serializers import AlumnoSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from  rest_framework import status
# un endPoint es un punto que nos permite interactuar con la ase de datos,(Generar Datos
# )

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

@ api_view(['GET','POST'])
def alumnos(request):
    if request.method == 'GET':
        alumnos= Alumno.objects.all()
        serilialized= AlumnoSerializers(alumnos, many= True)
        return Response(status=status.HTTP_200_OK, data=serilialized.data)

    if request.method == 'POST':
        alumno = AlumnoSerializers(data=request.data)
        if alumno.is_valid():
            alumno.save()
        return Response(status=status.HTTP_201_CREATED,
                        data={'detail':'Created'})

#a traves de esta vista se hace por un id en especifico
@ api_view(['GET','PUT','DELETE'])
def alumno_detalle(request,alumno_id):# definimos los parametros a utilizar dentro de las funciones
    alumno = Alumno.objects.get(id=alumno_id)#Obtenemos el parametro id del ojeto alumno
    if request.method == 'GET':
        serialized = AlumnoSerializers(alumno)
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    if request.method == 'PUT':
        serialized= AlumnoSerializers(instance=alumno,
                                      data= request.data,
                                      partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)
    if request.method== 'DELETE':
        alumno.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)


   #if request.method == 'DELETE':
    #   alumno.delete()
     #  return Response(status= status.HTTP_204_NO_CONTENT)



