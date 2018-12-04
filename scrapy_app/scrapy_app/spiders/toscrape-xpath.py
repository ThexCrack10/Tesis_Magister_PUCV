# -*- coding: utf-8 -*-
import scrapy
from scrapy import *
#VALIDAR SI SON NECESARIAS
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from scrapy_app.items import *
from scrapy.selector import HtmlXPathSelector
from scrapy.spiders import BaseSpider
import html2text

class ToScrapeSpiderXPath(CrawlSpider):
	name = 'deportes-xpath'
	allowed_domain = ['www.feriachilenadellibro.cl']
	start_urls = ['https://www.feriachilenadellibro.cl/deportes?product_list_mode=list']
	rules = {
		# Para cada item
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//*[@id="maincontent"]/div[2]/div[1]/div[6]/div[2]/ul/li[6]/a'))),
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//*[@id="maincontent"]/div[2]/div[1]/div[5]/ol/li/div/div/strong/a')),
										callback = 'parse_item', follow = False)
	}
	def parse_item(self, response):
		item = ScrapyProductoItem()
		#DATOS PRODUCTOS
		item['nombreProducto'] = response.xpath('//*[@id="maincontent"]/div[2]/div[1]/div[1]/div[1]/div/h1/span/text()').extract()
		item['descripcionProducto'] = response.xpath('//*[@id="product.info.description"]/div/div/p/text()').extract()
		item['tipoProducto'] = "Libros"
		#RELACION CATEGORIA - PRODUCTOS
		item['categoriaDestinoId'] = 3
		#RELACION CARACTERISTISCAS - PRODUCTO
		item['autorId'] = 6
		item['autor'] = response.xpath('//*[@id="product-attribute-specs-table"]/tbody/tr[2]/td/text()').extract()
		item['encuadernacionId'] = 7
		item['encuadernacion'] = response.xpath('//*[@id="product-attribute-specs-table"]/tbody/tr[5]/td/text()').extract()
		item['editorialId'] = 8
		item['editorial'] = response.xpath('//*[@id="product-attribute-specs-table"]/tbody/tr[4]/td/text()').extract()
		#VALOR MEDIDA
		item['unidadId'] = 3
		item['medidaValor'] = "Unidad"	
		#CODIGO PRODUCTO =RELACION TIPOCODIGO - PRODUCTO
		item['codigoISBNId'] = 5
		item['codigoSKUId'] = 6
		item['codigoISBN'] = response.xpath('//*[@id="product-attribute-specs-table"]/tbody/tr[3]/td/text()').extract()
		item['codigoSKU'] = response.xpath('//*[@id="maincontent"]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div/text()').extract()
		#PRECIO
		item['precioId'] = 3	
		item['tipoPrecio'] = "Internet"	
		item['valorPrecio'] = response.xpath('//*[@id="maincontent"]/div[2]/div[1]/div[1]/div[2]/div[3]/span[1]/span/span/span/text()').extract()
		yield item