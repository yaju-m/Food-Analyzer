from flask import Flask 
import json
from urllib.request import urlopen
import scraper


app = Flask(__name__)

food_id= scraper.call_this()

#@app.route('/food/<food_id>', methods = ['GET', 'POST'])
def find_info(food_id):
	final_cal_dict= {}
	count= 0
	while count <= len(food_id):
		url = 'http://api.nal.usda.gov/ndb/reports/?ndbno=' + str(food_id[count]) + '&type=f&format=json&api_key=3MNz36md1IPX44kwQVKy4s6z3OIC1akW4hRK3qlR'
		http = urlopen(url)
		data = http.read().decode('utf-8')
		food_data_json = json.loads(data)
		nutrients = food_data_json['report']['food']['nutrients']
		calories = [nutrient for nutrient in nutrients if nutrient['name'] == 'Energy' and nutrient['unit'] == 'kcal']
		final_cal_dict[food_data_json['report']['food']['name']= calories
		count += 1
	return final_cal_dict

@app.route('/calories/<recipe_id>', methods=['GET'])
def calculate_calories(recipe_id):
	ingredients = some_function()
	for ingredient in ingredients:
		usda_code = scraper.call_this(ingredient)[0]
		cal_dict = find_info(usda_code)
		print(cal_dict)
		
