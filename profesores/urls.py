from django.urls import path
from profesores.views import  get_profesores, get_profesor

app_name = 'profesores'
urlpatterns =[
        path('get_profesores/',get_profesores, name='lista_profesores'),
        path('<profesor_id>/', get_profesor, name='profesor_id'),
        ]

