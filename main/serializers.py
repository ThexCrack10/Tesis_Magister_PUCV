from main.models import *
from rest_framework import serializers

class RubroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RubroComercio
        fields = ('id', 'nombreRubro') 

class ComercioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comercio
        fields = ('id', 'nombreComercio', 'rubroId') 

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = ('id', 'nombreSucursal', 'direccionSucursal', 'paisSucursal', 'comercioId') 

class PrecioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Precio
        fields = ('id', 'tipoPrecio', 'valorPrecio', 'sucursalId', 'productoId') 

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ('id', 'nombreProducto', 'descripcionProducto', 'tipoProducto') 

class CodigoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodigoProducto
        fields = ('id', 'valorCodigo', 'codigoId', 'productoId') 

class TipoCodigoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoCodigo
        fields = ('id', 'nombreCodigo') 

class CaracteristicaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaracteristicaProducto
        fields = ('id', 'valorCaracteristica', 'caracteristicaId', 'productoId') 

class CaracteristicaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Caracteristica
        fields = ('id', 'nombreCaracteristica') 

class CategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProducto
        fields = ('id', 'categoriaId', 'productoId') 

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nombreCategoria', 'descripcionCategoria', 'categoriaPadreFlag') 

class ValorMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValorMedida
        fields = ('id', 'valorMedida', 'unidadId', 'productoId') 

class UnidadDeMedidaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UnidadDeMedida
        fields = ('id', 'nombreMedida') 
