from import_export import resources
from .models import *

class RubroResource(resources.ModelResource):
    class Meta:
        modelRubro = RubroComercio
        #msodel = RubroComercio
        
class ComercioResource(resources.ModelResource):
    class Meta:
        modelComercio = Comercio

class SucursalResource(resources.ModelResource):
    class Meta:
        modelSucursal = Sucursal

class PrecioResource(resources.ModelResource):
    class Meta:
        modelPrecio = Precio

class ProductoResource(resources.ModelResource):
    class Meta:
        model = Producto

class CodigoProductoResource(resources.ModelResource):
    class Meta:
        modelCodigoProducto = CodigoProducto

class TipoCodigoResource(resources.ModelResource):
    class Meta:
        modelTipoCodigo = TipoCodigo

class CaracteristicaProductoResource(resources.ModelResource):
    class Meta:
        modelCaracteristicaProducto = CaracteristicaProducto

class CaracteristicaResource(resources.ModelResource):
    class Meta:
        modelCaracteristica = Caracteristica

class CategoriaProductoResource(resources.ModelResource):
    class Meta:
        modelCategoriaProducto = CategoriaProducto

class CategoriaResource(resources.ModelResource):
    class Meta:
        modelCategoria = Categoria

class ValorMedidaResource(resources.ModelResource):
    class Meta:
        modelValorMedida = ValorMedida

class UnidadDeMedidaResource(resources.ModelResource):
    class Meta:
        modelUnidadDeMedida = UnidadDeMedida
