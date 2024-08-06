from django.contrib import admin
from inventario.models import *

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'categoria', 'presentacion', 'precio', 'created_at', 'updated_at')
    search_fields = ('nombre', 'marca__nombre', 'categoria__nombre')
    list_filter = ('marca', 'categoria', 'presentacion')
    ordering = ('nombre',)
    readonly_fields = ('created_at', 'updated_at')

class InventarioAdmin(admin.ModelAdmin):
    list_display = ('producto', 'created_at', 'updated_at')
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


