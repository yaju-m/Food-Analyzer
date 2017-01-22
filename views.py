from flask import Flask 
import json
from urllib.request import urlopen
import scraper

scraper.


app = Flask(__name__)

food_id= 

@app.route('/food/<food_id>', methods = ['GET', 'POST'])
def find_info(food_id):
	url = 'http://api.nal.usda.gov/ndb/reports/?ndbno=' + str(food_id[0]) + '&type=f&format=json&api_key=3MNz36md1IPX44kwQVKy4s6z3OIC1akW4hRK3qlR'
	http = urlopen(url)
	data = http.read().decode('utf-8')
	food_data_json = json.loads(data)
	nutrients = food_data_json['report']['food']['nutrients']
	calories = [nutrient for nutrient in nutrients if nutrient['name'] == 'Energy' and nutrient['unit'] == 'kcal']
	return calories
