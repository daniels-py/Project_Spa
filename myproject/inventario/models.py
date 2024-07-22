from django.db import models
 
from django.utils import timezone

# Create your models here.



# Modelo para representar categorías de productos
class Categoria(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre de la Categoría')
    descripcion = models.TextField(verbose_name='Descripción de la Categoría')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'


class Marca(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre de la Marca')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'


# Modelo para representar presentaciones de productos
class Presentacion(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre de la Presentación')
    descripcion = models.TextField(verbose_name='Descripción de la Presentación')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Presentación'
        verbose_name_plural = 'Presentaciones'


# Modelo para representar productos
class Producto(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre del Producto')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoría')
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, verbose_name='Marca')
    presentacion = models.ForeignKey(Presentacion, on_delete=models.CASCADE, verbose_name='Presentación')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    descripcion = models.TextField(verbose_name='Descripción')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    def __str__(self):
        return f'{self.nombre} - {self.marca.nombre} ({self.presentacion.nombre})'

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


# Modelo para representar el inventario de productos
class Inventario(models.Model):
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE, verbose_name='Producto')
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad en Inventario')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    def __str__(self):
        return f'{self.producto.nombre} - {self.cantidad} unidades'

    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'


# Modelo para representar compras de productos
class Compra(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Producto')
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad Comprada')
    fecha_compra = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Compra')

    def __str__(self):
        return f'Compra de {self.cantidad} {self.producto.nombre} en {self.fecha_compra}'

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'


# Modelo para representar ventas de productos
class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Producto')
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad Vendida')
    fecha_venta = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Venta')

    def __str__(self):
        return f'Venta de {self.cantidad} {self.producto.nombre} en {self.fecha_venta}'

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'


class CaracteristicaColor(models.Model):
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE, verbose_name='Producto')
    codigo_color = models.CharField(max_length=50, verbose_name='Código de Color')
    descripcion = models.TextField(verbose_name='Descripción del Color')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    def __str__(self):
        return f'{self.producto.nombre} - {self.codigo_color}'

    class Meta:
        verbose_name = 'Característica de Color'
        verbose_name_plural = 'Características de Color'
