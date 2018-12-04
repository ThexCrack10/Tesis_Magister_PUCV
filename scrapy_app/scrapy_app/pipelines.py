# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from main.models import *

class ScrapyAppPipeline(object):
    def process_item(self, item, spider):
        producto = Producto(nombreProducto=item.get('nombreProducto'), descripcionProducto=item.get('descripcionProducto'), tipoProducto=item.get('tipoProducto'))
        producto.save()
        categoriaProducto = CategoriaProducto(categoriaId= Categoria.objects.get(id=item.get('categoriaDestinoId')), productoId=  producto)
        categoriaProducto.save()
        caracteristicaProducto = CaracteristicaProducto(valorCaracteristica= item.get('autor'), caracteristicaId= Caracteristica.objects.get(id=item.get('autorId')), productoId=  producto)
        caracteristicaProducto.save()
        caracteristicaProducto1 = CaracteristicaProducto(valorCaracteristica=item.get('encuadernacion'), caracteristicaId=Caracteristica.objects.get(id=item.get('encuadernacionId')), productoId=  producto)
        caracteristicaProducto1.save()
        caracteristicaProducto2 = CaracteristicaProducto(valorCaracteristica=item.get('editorial'), caracteristicaId=Caracteristica.objects.get(id=item.get('editorialId')), productoId=  producto)
        caracteristicaProducto2.save()
        valorMedida = ValorMedida(valorUnidadMedida=item.get('medidaValor'), unidadId=UnidadDeMedida.objects.get(id=item.get('unidadId')),productoId=  producto)
        valorMedida.save()
        codigoProducto = CodigoProducto(valorCodigo=item.get('codigoISBN'), codigoId=TipoCodigo.objects.get(id=item.get('codigoISBNId')), productoId=  producto)
        codigoProducto.save()
        codigoProducto1 = CodigoProducto(valorCodigo=item.get('codigoSKU'), codigoId=TipoCodigo.objects.get(id=item.get('codigoSKUId')), productoId=  producto)
        codigoProducto1.save()
        precio = Precio(tipoPrecio=item.get('tipoPrecio'), valorPrecio=item.get('valorPrecio'), sucursalId= Sucursal.objects.get(id=item.get('precioId')), productoId= producto)
        precio.save()
        return item
        
        
