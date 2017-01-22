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
	ingredients= {}
	user_input = text_parser('6 pounds of bananas')[2] #variable assigned to input from user
	name = 'USDA_table_spider'
	start_urls = ['https://ndb.nal.usda.gov/ndb/search/list?ds=Standard%20Reference&qlookup=']
	final_dict= {}
	#startrequests()
	#callback function will be a selector
	#response = HtmlResponse(url=user_input, body=tbody) #url here depends on user input
	#Selector(response=response).xpath('//span/text()').extract()
	def parse(self, response):
		url = self.start_urls[0] + self.user_input  # change to whatever your url is
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
		final_dict[0]= percent_similar(self.user_input, self.ingredients)
		return final_dict

def call_this():
	spidey = USDATableSpider(scrapy.Spider)
	return spidey.parse(HtmlResponse(url=self.start_urls[0] + self.user_input, bpdy=tbody))


	
