from django.conf.urls import url
from rest_framework.routers import DefaultRouter 
from main.views import *

urlpatterns = [
    url(r'^Rubros/$', RubroList.as_view(), name='Rubros'),
    url(r'^Comercios/$', ComercioList.as_view(), name='Comercios'),
    url(r'^Sucursal/$', SucursalList.as_view(), name='Sucursal'),
    url(r'^Precios/$', PrecioList.as_view(), name='Precio'),
    url(r'^Productos/$', ProductoList.as_view(), name='Productos'),
    url(r'^CategoriasProducto/$', CategoriaProductoList.as_view(), name='CategoriasProducto'),
    url(r'^Categorias/$', CategoriaList.as_view(), name='Categorias'),
    url(r'^CaracteristicasProducto/$', CaracteristicaProductoList.as_view(), name='CaracteristicasProducto'),
    url(r'^Caracteristicas/$', CaracteristicaList.as_view(), name='Caracteristicas'),
    url(r'^ValorMedidas/$', ValorMedidaList.as_view(), name='ValorMedidas'),
    url(r'^UnidadDeMedidas/$', UnidadDeMedidaList.as_view(), name='UnidadDeMedidas'),
    url(r'^CodigoProductos/$', CodigoProductoList.as_view(), name='CodigoProductos'),
    url(r'^TiposCodigo/$', TipoCodigoList.as_view(), name='TiposCodigo')
]