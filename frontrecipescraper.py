import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from scrapy.crawler import CrawlerProcess
from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen

current_id = 0 

class RecipeSpider(scrapy.Spider):

	def __init__(self, spider, current_id):
		scrapy.Spider.__init__(self, spider)	

		self.ingredients= {}
		self.name = 'recipe_spider'
		self.current_url = ['http://allrecipes.com/recipe/'+ str(current_id)]
		self.final_dict= {}
		#startrequests()
		#callback function will be a selector
		#response = HtmlResponse(url=user_input, body=tbody) #url here depends on user input
		#Selector(response=response).xpath('//span/text()').extract()
	
	def parse(self, response):
		list_of_ingred=[]
		dict_of_recipes = {}
		counter= 0
		url = self.current_url[0]
		print(url)
		page = urlopen(url).read()
		soup = BeautifulSoup(page)
		for li in soup.find_all('li', {'class': 'checkList__line'}):
			inner_span = li.find('span') 
			print(inner_span.text)
			if inner_span.text and inner_span.text.lower() != 'add all ingredients to list':
				list_of_ingred.append(inner_span.text) 
		while list_of_ingred: 
			dict_of_recipes[counter]= list_of_ingred[0]
			counter += 1
			list_of_ingred= list_of_ingred[1:]
		print('sdfsafasdfsdfsaf', dict_of_recipes, type(dict_of_recipes))
		return dict_of_recipes

def call_this(current_id):	
	spidey = RecipeSpider(scrapy.Spider, current_id)
	print(spidey.current_url[0])
	return spidey.parse(HtmlResponse(url=spidey.current_url[0]))
