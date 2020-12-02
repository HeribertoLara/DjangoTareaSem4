from django.urls import path
from clases.views import  clases_views,get_clase,get_clases

app_name= 'clases'
urlpatterns =[
        path('',clases_views, name='clasesviews'),
        path('get_clases/',get_clases, name='lista_clases'),
        path('<clase_id>/', get_clase, name='materia_id'),
        ]
