import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from scrapy.crawler import CrawlerProcess
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

class USDATableSpider(scrapy.Spider):
	ingredients= {}
	user_input = 'x' #variable assigned to input from user
	name = 'USDA_table_spider'
	start_urls = ['https://ndb.nal.usda.gov/ndb/search/list?ds=Standard%20Reference&qlookup=']
	#startrequests()
	#callback function will be a selector
	#response = HtmlResponse(url=user_input, body=tbody) #url here depends on user input
	#Selector(response=response).xpath('//span/text()').extract()
	def parse(self, response):
		url = self.start_urls[0] + self.user_input  # change to whatever your url is
		page = urlopen(url).read()
		soup = BeautifulSoup(page)
		for tr in soup.find_all('tr')[1:]:
<<<<<<< HEAD
			tds = tr.find_all('td')
			number = str(tds[0].text)
			food = str(tds[1].text)
			number= number.replace('\t', '')
			number= number.replace('\n', '')
			food= food.replace('\t', '')
			food= food.replace('\n', '')
			self.ingredients[number]= food
			print(self.ingredients)
=======
    			tds = tr.find_all('td')
			tds[0]= re.sub('\s+', '', tds[0])
			tds[1]= re.sub('\s+', '', tds[1])
    			self.ingredients[tds[0].text]= tds[1].text
    			print(self.ingredients)
>>>>>>> 680501eec1c0db2da60d1d67b9934bf78a8fca1d
		
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(USDATableSpider)
process.start()	
	
