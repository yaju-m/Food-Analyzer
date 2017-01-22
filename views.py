from flask import Flask 
import json
from urllib.request import urlopen
import scraper
import frontrecipescraper

app = Flask(__name__)

def find_info(food_id):
	url = 'http://api.nal.usda.gov/ndb/reports/?ndbno=' + str(food_id) + '&type=f&format=json&api_key=3MNz36md1IPX44kwQVKy4s6z3OIC1akW4hRK3qlR'
	print(url)
	http = urlopen(url)
	data = http.read().decode('utf-8')
	food_data_json = json.loads(data)
	nutrients = food_data_json['report']['food']['nutrients']
	calories = [nutrient for nutrient in nutrients if nutrient['name'] == 'Energy' and nutrient['unit'] == 'kcal']
	return calories

@app.route('/calories/<recipe_id>', methods=['GET'])
def calculate_calories(recipe_id):
	ingredients = frontrecipescraper.call_this(recipe_id) 
	print('\n\n\nasdf2', ingredients, type(ingredients), '\n\n\n')
	for _, ingredient in ingredients.items():
		print('asdf3', ingredient)
		usda_code = scraper.call_this(ingredient)[0]
		if usda_code == -1:
			continue
		cal_dict = find_info(usda_code)
		print(cal_dict)
	return recipe_id
	

if __name__ == "__main__":
	app.run(debug=True)	
