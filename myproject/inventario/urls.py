from django.urls import path
from .views import *



 # en este podermos redireccionar las vista a archivos html que estemos utilizando 

urlpatterns = [
    #  nombre de la direccion luego nombre de la funcion depues un indicativo de esa pagina 
    path('Principal',Portada,name="Principal"),
]