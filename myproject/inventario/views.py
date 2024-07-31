
from django.shortcuts import render
from django.views import View
from inventario.models import *
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.  se crean los modelos CRUD para la implementacion de nuestra aplicacion 

#nombre de la funcion que espera una respuesta para luego retornar un esa misma repsuesta en un archivo html esto no es chat GPT
def Portada(request):
    return render(request,"index.html")



#creacion del Crud

class ListarCategorias(View):
    def get(self, request):
        datos = Categoria.objects.all()
        datos_categorias = [{'nombre': i.nombre, 'descripcion': i.descripcion} for i in datos]
        return JsonResponse(datos_categorias, safe=False)



@method_decorator(csrf_exempt, name='dispatch')
class CrearCategoria(View):
    def post(self, request):
        try:
            # Cargar datos del request
            data = json.loads(request.body)
            nombre = data.get('nombre')
            descripcion = data.get('descripcion')

            if not nombre:
                return JsonResponse({'error': 'Nombre es obligatorio'}, status=400)

            # Crear y guardar la nueva categoría
            nueva_categoria = Categoria(nombre=nombre, descripcion=descripcion)
            nueva_categoria.save()

            return JsonResponse({
                'mesage': 'Categoria registrada con éxito',
                'id': nueva_categoria.id,
                'nombre': nueva_categoria.nombre,
                'descripcion': nueva_categoria.descripcion
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Datos inválidos'}, status=400)

        except Exception as e:
            # Manejo general de excepciones
            return JsonResponse({'error': str(e)}, status=500)






class ListarMarcas(View):
    def get(self, request):
        datos = Marca.objects.all()
        datos_marcas = [{'nombre': i.nombre} for i in datos]
        return JsonResponse(datos_marcas, safe=False)


class ListarPresentaciones(View):
    def get(self, request):
        datos = Presentacion.objects.all()
        datos_presentaciones = [{'nombre': i.nombre, 'descripcion': i.descripcion} for i in datos]
        return JsonResponse(datos_presentaciones, safe=False)


class ListarProductos(View):
    def get(self, request):
        datos = Producto.objects.all()
        datos_productos = [{
            'nombre': i.nombre,
            'categoria': i.categoria.nombre,
            'marca': i.marca.nombre,
            'presentacion': i.presentacion.nombre,
            'precio': i.precio,
            'descripcion': i.descripcion,
            'created_at': i.created_at,
            'updated_at': i.updated_at
        } for i in datos]
        return JsonResponse(datos_productos, safe=False)


class ListarInventarios(View):
    def get(self, request):
        datos = Inventario.objects.all()
        datos_inventarios = [{
            'producto': i.producto.nombre,
            'cantidad': i.cantidad,
            'created_at': i.created_at,
            'updated_at': i.updated_at
        } for i in datos]
        return JsonResponse(datos_inventarios, safe=False)


class ListarCompras(View):
    def get(self, request):
        datos = Compra.objects.all()
        datos_compras = [{
            'producto': i.producto.nombre,
            'cantidad': i.cantidad,
            'fecha_compra': i.fecha_compra
        } for i in datos]
        return JsonResponse(datos_compras, safe=False)


class ListarVentas(View):
    def get(self, request):
        datos = Venta.objects.all()
        datos_ventas = [{
            'producto': i.producto.nombre,
            'cantidad': i.cantidad,
            'fecha_venta': i.fecha_venta
        } for i in datos]
        return JsonResponse(datos_ventas, safe=False)


class ListarCaracteristicasColor(View):
    def get(self, request):
        datos = CaracteristicaColor.objects.all()
        datos_caracteristicas_color = [{
            'producto': i.producto.nombre,
            'codigo_color': i.codigo_color,
            'descripcion': i.descripcion,
            'created_at': i.created_at,
            'updated_at': i.updated_at
        } for i in datos]
        return JsonResponse(datos_caracteristicas_color, safe=False)