import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from scrapy.crawler import CrawlerProcess
from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen
from GoogleNLP import parse as text_parser
from difflib import SequenceMatcher

def percent_similar(query, ingredients):
	percentages = [SequenceMatcher(None, query, i).ratio() for i in ingredients]
	best_match = max(percentages)
	correct_index= percentages.index(best_match)
	list_of_foods= list(ingredients.keys())
	return ingredients[list_of_foods[correct_index]]


class RecipeSpider(scrapy.Spider):
	ingredients= {}
	#variable assigned to input from user
	name = 'recipe_spider'
	start_urls = ['https://allrecipes.com/recipes/']
	final_dict= {}
	#startrequests()
	#callback function will be a selector
	#response = HtmlResponse(url=user_input, body=tbody) #url here depends on user input
	#Selector(response=response).xpath('//span/text()').extract()
	def parse(self, response):
		list_of_recipes=[]
		dict_of_recipes = {}
		url= start_urls[0]
		page= urlopen(url).read()
		soup = BeautifulSoup(page)
		for h3 in soup.find_all('h3')[:]:
			atags = h3.find_all('a')
			list_of_recipes += [atags]
			#need a list of hrefs in h3 in a. call is href_list
		for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
			if link.has_attr('href=/recipe/'):
				while list_of_recipes and href_list:
					dict_of_recipes[list_of_recipes[0]] = href_list[0]
					list_of_recipes= list_of_recipes[1:]
					href_list= href_list[1:]	
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

def call_this():
	spidey = USDATableSpider(scrapy.Spider)
	return spidey.parse(HtmlResponse(url=spidey.start_urls[0] + spidey.user_input))
