# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ScrapyProductoItem(scrapy.Item):
    #DATOS PRODUCTOS
    nombreProducto = scrapy.Field()
    descripcionProducto = scrapy.Field()
    tipoProducto = scrapy.Field()
    #RELACION CATEGORIA - PRODUCTOS
    categoriaDestinoId = scrapy.Field()
    #RELACION CARACTERISTISCAS - PRODUCTO
    autorId = scrapy.Field()
    autor = scrapy.Field()
    encuadernacionId = scrapy.Field()
    encuadernacion = scrapy.Field()
    editorialId = scrapy.Field()
    editorial = scrapy.Field()
    #RELACION UNIDADDEMEDIDA - PRODUCTO
    medidaValor = scrapy.Field()
    unidadId = scrapy.Field()
    #CODIGO PRODUCTO =RELACION TIPOCODIGO - PRODUCTO
    codigoISBNId = scrapy.Field()
    codigoSKUId = scrapy.Field()
    codigoISBN = scrapy.Field()
    codigoSKU = scrapy.Field()
    #PRECIO
    tipoPrecio = scrapy.Field()
    valorPrecio = scrapy.Field()
    precioId = scrapy.Field()
    #pass
