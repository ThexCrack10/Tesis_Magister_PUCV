# -*- coding: utf-8 -*-
import scrapy
#VALIDAR SI SON NECESARIAS
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from scrapy_app.items import *
from scrapy.selector import HtmlXPathSelector
from scrapy.spiders import BaseSpider
import html2text

"""
class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                'text': quote.css("span.text::text").extract_first(),
                'author': quote.css("small.author::text").extract_first(),
                'tags': quote.css("div.tags > a.tag::text").extract()
            }

        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
"""

class ToScrapeCSSSpider(scrapy.Spider):
	name = 'deportes-css'
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
		item['nombreProducto'] = response.xpath('//*[@id="maincontent"]/div[2]/div[1]/div[1]/div[1]/div/h1/span/text()').extract()
		item['descripcionProducto'] = response.xpath('//*[@id="product.info.description"]/div/div/p/text()').extract()
		item['tipoProducto'] = response.xpath('//*[@id="maincontent"]/div[2]/div[1]/div[1]/div[2]/div[3]/span[1]/span/span/span/text()').extract()
		#item['autor'] = response.xpath('//*[@id="product-attribute-specs-table"]/tbody/tr[2]/td/text()').extract()
		#item['codigo'] = response.xpath('//*[@id="maincontent"]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div/text()').extract()
		yield item
		
			

