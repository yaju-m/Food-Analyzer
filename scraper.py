import scrapy

class USDATableSpider(scrapy.Spider):
	name = 'USDA_table_spider'
	start_urls = ['https://ndb.nal.usda.gov/ndb/search/list?ds=Standard%20Reference&qlookup']

	def parse(self, response):