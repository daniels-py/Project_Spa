from django.contrib import admin
from inventario.models import *
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la vista de lista del administrador.
    list_display = ('nombre', 'marca', 'categoria', 'presentacion','precio', 'created_at', 'updated_at')
    # Campos en los que se puede buscar en la vista de lista.
    search_fields = ('nombre', 'marca__nombre', 'categoria__nombre')
    # Filtros disponibles en la barra lateral para facilitar la búsqueda.
    list_filter = ('marca', 'categoria', 'presentacion')
    # Orden predeterminado en que se muestran los registros.
    ordering = ('nombre',)
    # Campos que son de solo lectura y no se pueden editar.
    readonly_fields = ('created_at', 'updated_at')

class InventarioAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad', 'created_at', 'updated_at')
    search_fields = ('producto__nombre',)
    readonly_fields = ('created_at', 'updated_at')

class CompraAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad', 'fecha_compra')
    search_fields = ('producto__nombre',)
    list_filter = ('fecha_compra',)

class VentaAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad', 'fecha_venta')
    search_fields = ('producto__nombre',)
    list_filter = ('fecha_venta',)


class CaracteristicaColorAdmin(admin.ModelAdmin):
    list_display = ('producto', 'codigo_color', 'descripcion')
    search_fields = ('producto__nombre', 'codigo_color')
    list_filter = ('producto',)
    readonly_fields = ('created_at', 'updated_at')



# Registra el modelo Categoria en la interfaz de administración con configuración por defecto.
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Presentacion)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Inventario, InventarioAdmin)
admin.site.register(Compra, CompraAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(CaracteristicaColor, CaracteristicaColorAdmin)


#usuario danielito


