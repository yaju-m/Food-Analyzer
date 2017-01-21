import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from bs4 import BeautifulSoup
import urllib.request import urlopen

class USDATableSpider(scrapy.Spider):
	ingredients= {}
	user_input = 'x' #variable assigned to input from user
	name = 'USDA_table_spider'
	start_urls = ['https://ndb.nal.usda.gov/ndb/search/list?ds=Standard%20Reference&qlookup=']
	startrequests()
	#callback function will be a selector
	#response = HtmlResponse(url=user_input, body=tbody) #url here depends on user input
	#Selector(response=response).xpath('//span/text()').extract()
	def parse(self, response):
		url = start_urls[0] + user_input  # change to whatever your url is
		page = urllib2.urlopen(url).read()
		soup = BeautifulSoup(page)
		for tr in soup.find_all('tr')[1:]:
    			tds = tr.find_all('td')
			ingredients[tds[0].text]= tds[1].text
		
	parse(self, response)
	
	
	
		
