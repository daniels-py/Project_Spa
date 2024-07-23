from django.urls import path
from .views import *



 # en este podermos redireccionar las vista a archivos html que estemos utilizando 

urlpatterns = [
    path('', index, name="admin-index"),
]