from django.urls import path
from .views import (
    Portada, ListarCategorias, CrearCategoria, ListarMarcas, CrearMarca,
    ListarPresentaciones, CrearPresentacion, ListarProductos, CrearProducto,
    BuscarProductoPorCodigo, ListarInventarios, AgregarAlInventario, ListarCompras,
    ListarVentas, ListarCaracteristicasColor, CrearCaracteristicaColor
)

urlpatterns = [
    # Página principal
    path('Principal/', Portada, name="Principal"),

    # Categorías
    path('categorias/', ListarCategorias.as_view(), name='listar_categorias'),
    path('categorias/crear/', CrearCategoria.as_view(), name='crear_categoria'),

    # Marcas
    path('marcas/', ListarMarcas.as_view(), name='listar_marcas'),
    path('marcas/crear/', CrearMarca.as_view(), name='crear_marca'),

    # Presentaciones
    path('presentaciones/', ListarPresentaciones.as_view(), name='listar_presentaciones'),
    path('presentaciones/crear/', CrearPresentacion.as_view(), name='crear_presentacion'),

    # Productos
    path('productos/', ListarProductos.as_view(), name='listar_productos'),
    path('productos/crear/', CrearProducto.as_view(), name='crear_producto'),
    path('productos/buscar/<str:codigo_producto>/', BuscarProductoPorCodigo.as_view(), name='buscar_producto'),

    # Inventarios
    path('inventarios/', ListarInventarios.as_view(), name='listar_inventarios'),
    path('inventarios/agregar/', AgregarAlInventario.as_view(), name='agregar_al_inventario'),

    # Compras
    path('compras/', ListarCompras.as_view(), name='listar_compras'),

    # Ventas
    path('ventas/', ListarVentas.as_view(), name='listar_ventas'),

    # Características de Color
    path('caracteristicas_color/', ListarCaracteristicasColor.as_view(), name='listar_caracteristicas_color'),
    path('caracteristicas_color/crear/', CrearCaracteristicaColor.as_view(), name='crear_caracteristica_color'),
]

