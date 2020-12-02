from django.urls import path
from alumnos.views import alumnos_views, get_alumnos, alumnos,alumno_detalle

app_name = 'alumnos'
urlpatterns = [
    path('alumnos_views/',alumnos_views, name= 'alumnos_views'),
    path('lista_alumnos/',get_alumnos, name='alumnos_list'),
    path('alumnos_serialized/', alumnos, name='alumnos'),
    path('<alumno_id>', alumno_detalle, name='alumnos_detalle')
]
