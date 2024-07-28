from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.  se crean los modelos CRUD para la implementacion de nuestra aplicacion 

#nombre de la funcion que espera una respuesta para luego retornar un esa misma repsuesta en un archivo html esto no es chat GPT
def Portada(request):
    return render(request,"index.html")


