from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.  se crean los modelos CRUD para la implementacion de nuestra aplicacion 

def index(request):
    return HttpResponse('Hola mundo')