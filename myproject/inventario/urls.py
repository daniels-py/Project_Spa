from django.urls import path
from .views import *



 # en este podermos redireccionar las vista a archivos html que estemos utilizando 

urlpatterns = [
    #  nombre de la direccion luego nombre de la funcion depues un indicativo de esa pagina 
    path('Principal',Portada,name="Principal"),
    path('categorias/', ListarCategorias.as_view(), name='listar_categorias'),
    path('categorias/crear/', CrearCategoria.as_view(), name='crear_categoria'),
    path('marcas/', ListarMarcas.as_view(), name='listar_marcas'),
    path('presentaciones/', ListarPresentaciones.as_view(), name='listar_presentaciones'),
    path('productos/', ListarProductos.as_view(), name='listar_productos'),
    path('inventarios/', ListarInventarios.as_view(), name='listar_inventarios'),
    path('compras/', ListarCompras.as_view(), name='listar_compras'),
    path('ventas/', ListarVentas.as_view(), name='listar_ventas'),
    path('caracteristicas_color/', ListarCaracteristicasColor.as_view(), name='listar_caracteristicas_color'),
]