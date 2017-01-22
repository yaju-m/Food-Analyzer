import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from scrapy.crawler import CrawlerProcess
from bs4 import BeautifulSoup
from urllib.request import urlopen
from GoogleNLP import parse as text_parser
from difflib import SequenceMatcher

def percent_similar(query, ingredients):
	percentages = [SequenceMatcher(None, query, i).ratio() for i in ingredients]
	best_match = max(percentages)
	correct_index= percentages.index(best_match)
	list_of_foods= list(ingredients.keys())
	return ingredients[list_of_foods[correct_index]]


class USDATableSpider(scrapy.Spider):

	def __init__(self, spider, query):
		scrapy.Spider.__init__(self, spider)
		self.query = query
		self.ingredients= {}
		result = text_parser(self.query) #variable assigned to input from user
		self.user_input = result[2]
		#print(result)
		self.final_dict = {}
		self.name = 'USDA_table_spider'
		self.start_urls = ['https://ndb.nal.usda.gov/ndb/search/list?ds=Standard%20Reference&qlookup=']

	#startrequests()
	#callback function will be a selector
	#response = HtmlResponse(url=user_input, body=tbody) #url here depends on user input
	#Selector(response=response).xpath('//span/text()').extract()
	def parse(self, response):
		url = self.start_urls[0] + self.user_input  # change to whatever your url is
		url = url.replace(" ", "%20")
		page = urlopen(url).read()
		soup = BeautifulSoup(page)
		for tr in soup.find_all('tr')[1:]:
			tds = tr.find_all('td')
			number = str(tds[0].text)
			food = str(tds[1].text)
			number= number.replace('\t', '')
			number= number.replace('\n', '')
			food= food.replace('\t', '')
			food= food.replace('\n', '')
			self.ingredients[food]= number
		self.final_dict[0]= percent_similar(self.user_input, self.ingredients)
		return self.final_dict

def call_this(query):
	query = query.replace("teaspoon", "tsp")
	query = query.replace("teaspoons", "tsp")
	query = query.replace("skinless", "no")
	spidey = USDATableSpider(scrapy.Spider, query)
	return spidey.parse(HtmlResponse(url=spidey.start_urls[0] + spidey.user_input))
