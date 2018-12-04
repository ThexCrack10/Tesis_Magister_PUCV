from django.contrib import admin
#from main.models import Quote
from main.models import *
#MODELO ANTERIOR
from import_export.admin import ImportExportModelAdmin
from django.contrib.admin import AdminSite
#CARGA MASIVA   
from django import forms
from django.urls import path
from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Count

from import_export import resources
import tablib

#class ProductoAdmin(admin.ModelAdmin):
class ProductoAdmin(ImportExportModelAdmin):
    list_display = ('nombreProducto', 'descripcionProducto','tipoProducto', )

class RubroComercioAdmin(admin.ModelAdmin):
    list_display = ('nombreRubro', )

class ComercioAdmin(admin.ModelAdmin):
    list_display = ('nombreComercio', 'rubroId', )

class SucursalAdmin(admin.ModelAdmin):
    list_display = ('nombreSucursal', 'direccionSucursal','paisSucursal', 'comercioId', )

class PrecioAdmin(admin.ModelAdmin):
    list_display = ('tipoPrecio', 'valorPrecio','sucursalId', 'productoId')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombreCategoria', 'descripcionCategoria','categoriaPadreFlag', )

class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display = ('categoriaId', 'productoId', )

class CaracteristicaAdmin(admin.ModelAdmin):
    list_display = ('nombreCaracteristica', )

class CaracteristicaProductoAdmin(admin.ModelAdmin):
    list_display = ('valorCaracteristica', 'caracteristicaId','productoId', )

class UnidadDeMedidaAdmin(admin.ModelAdmin):
    list_display = ('nombreMedida', )

class ValorMedidaAdmin(admin.ModelAdmin):
    list_display = ('valorUnidadMedida', 'unidadId','productoId', )

class TipoCodigoAdmin(admin.ModelAdmin):
    list_display = ('nombreCodigo', )

class CodigoProductoAdmin(admin.ModelAdmin):
    list_display = ('valorCodigo', 'codigoId','productoId', )

# Register your models here.
admin.site.register(Producto, ProductoAdmin)
admin.site.register(RubroComercio,RubroComercioAdmin)
admin.site.register(Comercio,ComercioAdmin)
admin.site.register(Sucursal,SucursalAdmin)
admin.site.register(Precio,PrecioAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(CategoriaProducto,CategoriaProductoAdmin)
admin.site.register(Caracteristica, CaracteristicaAdmin)
admin.site.register(CaracteristicaProducto, CaracteristicaProductoAdmin)
admin.site.register(UnidadDeMedida,UnidadDeMedidaAdmin)
admin.site.register(ValorMedida,ValorMedidaAdmin)
admin.site.register(TipoCodigo,TipoCodigoAdmin)                 
admin.site.register(CodigoProducto,CodigoProductoAdmin)  