import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from scrapy.crawler import CrawlerProcess
from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen

current_id = 0 

class RecipeSpider(scrapy.Spider):
	ingredients= {}
	#variable assigned to input from user
	name = 'recipe_spider'
	current_url = ['https://allrecipes.com/recipes/'+ str(current_id)]
	final_dict= {}
	#startrequests()
	#callback function will be a selector
	#response = HtmlResponse(url=user_input, body=tbody) #url here depends on user input
	#Selector(response=response).xpath('//span/text()').extract()
	def parse(self, response):
		list_of_ingred=[]
		dict_of_recipes = {}
		counter= 0
		url= current_url
		page= urlopen(url).read()
		soup = BeautifulSoup(page)
		for ul in soup.find_all('ul'): 
			for li in soup.find_all('li', {'class': 'checklist__line'}): 
				list_of_ingred += [li]
		while list_of_ingred: 
			dict_of_recipes[counter]= list_of_ingred[0]
			counter += 1
			list_of_ingred= list_of_ingred[1:]
		return dict_of_recipes

def call_this():
	spidey = RecipeSpider(scrapy.Spider)
	return spidey.parse(HtmlResponse(url=current_url))
