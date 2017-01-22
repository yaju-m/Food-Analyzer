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
		self.user_input = text_parser(self.query)[2] #variable assigned to input from user
		self.name = 'USDA_table_spider'
		self.start_urls = ['https://ndb.nal.usda.gov/ndb/search/list?ds=Standard%20Reference&qlookup=']
		self.final_dict= {}

	#startrequests()
	#callback function will be a selector
	#response = HtmlResponse(url=user_input, body=tbody) #url here depends on user input
	#Selector(response=response).xpath('//span/text()').extract()
	def parse(self, response):
		list_of_recipes=[]
		url= start_urls[0]
		page= urlopen(url).read()
		soup = BeautifulSoup(page)
		for h3 in soup.find_all('h3')[:]:
			atags = h3.find_all('a')
			list_of_recipes += [atags]
			url = self.start_urls[0] +   # change to whatever your url is
			page = urlopen(url).read()


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
	spidey = USDATableSpider(scrapy.Spider, query)
	return spidey.parse(HtmlResponse(url=spidey.start_urls[0] + spidey.user_input))
