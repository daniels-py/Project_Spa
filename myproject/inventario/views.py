from django.shortcuts import render
from django.views import View
from inventario.models import *
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

def Portada(request):
    return render(request, "index.html")

# Categorías
class ListarCategorias(View):
    def get(self, request):
        datos = Categoria.objects.all()
        datos_categorias = [{'nombre': i.nombre, 'descripcion': i.descripcion} for i in datos]
        return JsonResponse(datos_categorias, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class CrearCategoria(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            nombre = data.get('nombre')
            descripcion = data.get('descripcion')

            if not nombre:
                return JsonResponse({'error': 'Nombre es obligatorio'}, status=400)

            nueva_categoria = Categoria(nombre=nombre, descripcion=descripcion)
            nueva_categoria.save()

            return JsonResponse({
                'message': 'Categoría registrada con éxito',
                'id': nueva_categoria.id,
                'nombre': nueva_categoria.nombre,
                'descripcion': nueva_categoria.descripcion
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Datos inválidos'}, status=400)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

# Marcas
class ListarMarcas(View):
    def get(self, request):
        datos = Marca.objects.all()
        datos_marcas = [{'nombre': i.nombre} for i in datos]
        return JsonResponse(datos_marcas, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class CrearMarca(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            nombre = data.get('nombre')

            if not nombre:
                return JsonResponse({'error': 'Nombre es obligatorio'}, status=400)

            nueva_marca = Marca(nombre=nombre)
            nueva_marca.save()

            return JsonResponse({
                'message': 'Marca registrada con éxito',
                'id': nueva_marca.id,
                'nombre': nueva_marca.nombre
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Datos inválidos'}, status=400)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

# Presentaciones
class ListarPresentaciones(View):
    def get(self, request):
        datos = Presentacion.objects.all()
        datos_presentaciones = [{'nombre': i.nombre, 'descripcion': i.descripcion} for i in datos]
        return JsonResponse(datos_presentaciones, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class CrearPresentacion(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            nombre = data.get('nombre')
            descripcion = data.get('descripcion')

            if not nombre:
                return JsonResponse({'error': 'Nombre es obligatorio'}, status=400)

            nueva_presentacion = Presentacion(nombre=nombre, descripcion=descripcion)
            nueva_presentacion.save()

            return JsonResponse({
                'message': 'Presentación registrada con éxito',
                'id': nueva_presentacion.id,
                'nombre': nueva_presentacion.nombre,
                'descripcion': nueva_presentacion.descripcion
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Datos inválidos'}, status=400)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

# Productos
class ListarProductos(View):
    def get(self, request):
        datos = Producto.objects.all()
        datos_productos = []
        
        for i in datos:
            caracteristica_color = CaracteristicaColor.objects.filter(producto=i).first()
            datos_productos.append({
                'codigo_producto': i.codigo_producto,
                'nombre': i.nombre,
                'categoria': i.categoria.nombre,
                'marca': i.marca.nombre,
                'presentacion': i.presentacion.nombre,
                'precio': i.precio,
                'descripcion': i.descripcion,
                'cantidad': i.cantidad,  # Ahora está en Producto
                'created_at': i.created_at,
                'updated_at': i.updated_at,
                'caracteristica_color': {
                    'codigo_color': caracteristica_color.codigo_color if caracteristica_color else 'No tiene característica de color',
                    'descripcion': caracteristica_color.descripcion if caracteristica_color else 'No tiene característica de color'
                }
            })
        
        return JsonResponse(datos_productos, safe=False)

class BuscarProductoPorCodigo(View):
    def get(self, request, codigo_producto):
        try:
            producto = Producto.objects.get(codigo_producto=codigo_producto)
            caracteristica_color = CaracteristicaColor.objects.filter(producto=producto).first()
            datos_producto = {
                'message': 'Producto encontrado con éxito',
                'codigo_producto': producto.codigo_producto,
                'nombre': producto.nombre,
                'categoria': producto.categoria.nombre,
                'marca': producto.marca.nombre,
                'presentacion': producto.presentacion.nombre,
                'precio': producto.precio,
                'descripcion': producto.descripcion,
                'cantidad': producto.cantidad,  # Ahora está en Producto
                'created_at': producto.created_at,
                'updated_at': producto.updated_at,
                'caracteristica_color': {
                    'codigo_color': caracteristica_color.codigo_color if caracteristica_color else 'No tiene característica de color',
                    'descripcion': caracteristica_color.descripcion if caracteristica_color else 'No tiene característica de color'
                }
            }
            return JsonResponse(datos_producto, safe=False)
        except Producto.DoesNotExist:
            return JsonResponse({'error': 'Producto no encontrado'}, status=404)

@method_decorator(csrf_exempt, name='dispatch')
class CrearProducto(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            codigo_producto = data.get('codigo_producto')
            nombre = data.get('nombre')
            categoria_id = data.get('categoria_id')
            marca_id = data.get('marca_id')
            presentacion_id = data.get('presentacion_id')
            precio = data.get('precio')
            descripcion = data.get('descripcion')
            cantidad = data.get('cantidad', 0)  # Agregar cantidad al crear producto

            if not codigo_producto or not nombre or not categoria_id or not marca_id or not presentacion_id or not precio:
                return JsonResponse({'error': 'Todos los campos son obligatorios'}, status=400)

            try:
                precio = precio.replace(',', '')
                precio = float(precio)
            except ValueError:
                return JsonResponse({'error': 'Precio inválido'}, status=400)

            if precio < 0:
                return JsonResponse({'error': 'El precio no puede ser negativo'}, status=400)

            categoria = Categoria.objects.get(id=categoria_id)
            marca = Marca.objects.get(id=marca_id)
            presentacion = Presentacion.objects.get(id=presentacion_id)

            nuevo_producto = Producto(
                codigo_producto=codigo_producto,
                nombre=nombre,
                categoria=categoria,
                marca=marca,
                presentacion=presentacion,
                precio=precio,
                descripcion=descripcion,
                cantidad=cantidad  # Establecer cantidad al crear producto
            )
            nuevo_producto.save()

            return JsonResponse({
                'message': 'Producto registrado con éxito',
                'id': nuevo_producto.id,
                'codigo_producto': nuevo_producto.codigo_producto,
                'nombre': nuevo_producto.nombre,
                'categoria': nuevo_producto.categoria.nombre,
                'marca': nuevo_producto.marca.nombre,
                'presentacion': nuevo_producto.presentacion.nombre,
                'precio': nuevo_producto.precio,
                'descripcion': nuevo_producto.descripcion,
                'cantidad': nuevo_producto.cantidad
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Datos inválidos'}, status=400)

        except Categoria.DoesNotExist:
            return JsonResponse({'error': 'Categoría no encontrada'}, status=404)

        except Marca.DoesNotExist:
            return JsonResponse({'error': 'Marca no encontrada'}, status=404)

        except Presentacion.DoesNotExist:
            return JsonResponse({'error': 'Presentación no encontrada'}, status=404)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

# Inventario
class ListarInventarios(View):
    def get(self, request):
        datos = Producto.objects.all()  # Listar productos en lugar de Inventario
        datos_inventarios = [{
            'codigo_producto': i.codigo_producto,
            'producto': i.nombre,
            'cantidad': i.cantidad,  # Ahora en Producto
            'created_at': i.created_at,
            'updated_at': i.updated_at
        } for i in datos]
        return JsonResponse(datos_inventarios, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class AgregarAlInventario(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            producto_id = data.get('producto_id')

            if not producto_id:
                return JsonResponse({'error': 'El ID del producto es obligatorio'}, status=400)

            try:
                producto = Producto.objects.get(id=producto_id)
            except Producto.DoesNotExist:
                return JsonResponse({'error': 'Producto no encontrado'}, status=404)

            # Verificar si el producto ya está en el inventario
            inventario, created = Inventario.objects.get_or_create(producto=producto)

            if created:
                inventario.save()

            return JsonResponse({
                'message': 'Producto añadido al inventario con éxito',
                'producto': producto.nombre
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Datos inválidos'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
# Compras
class ListarCompras(View):
    def get(self, request):
        datos = Compra.objects.all()
        datos_compras = [{
            'producto': i.producto.nombre,
            'cantidad': i.cantidad,
            'fecha_compra': i.fecha_compra
        } for i in datos]
        return JsonResponse(datos_compras, safe=False)

# Ventas
class ListarVentas(View):
    def get(self, request):
        datos = Venta.objects.all()
        datos_ventas = [{
            'producto': i.producto.nombre,
            'cantidad': i.cantidad,
            'fecha_venta': i.fecha_venta
        } for i in datos]
        return JsonResponse(datos_ventas, safe=False)

# Características por color
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

@method_decorator(csrf_exempt, name='dispatch')
class CrearCaracteristicaColor(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            producto_id = data.get('producto_id')
            codigo_color = data.get('codigo_color')
            descripcion = data.get('descripcion')

            if not producto_id or not codigo_color:
                return JsonResponse({'error': 'Producto y código de color son obligatorios'}, status=400)

            producto = Producto.objects.get(id=producto_id)

            caracteristica_color = CaracteristicaColor(
                producto=producto,
                codigo_color=codigo_color,
                descripcion=descripcion
            )
            caracteristica_color.save()

            # Actualizar el producto para indicar que tiene una característica de color
            producto.tiene_caracteristica_color = True
            producto.save()

            return JsonResponse({
                'message': 'Característica de color registrada con éxito',
                'id': caracteristica_color.id,
                'producto': producto.nombre,
                'codigo_color': caracteristica_color.codigo_color,
                'descripcion': caracteristica_color.descripcion
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Datos inválidos'}, status=400)

        except Producto.DoesNotExist:
            return JsonResponse({'error': 'Producto no encontrado'}, status=404)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
