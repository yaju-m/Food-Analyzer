from flask import Flask, jsonify 
import json
from urllib.request import urlopen
import scraper
import frontrecipescraper

app = Flask(__name__)

results_cache = {}

def find_info(food_id):
	url = 'http://api.nal.usda.gov/ndb/reports/?ndbno=' + str(food_id) + '&type=f&format=json&api_key=MwnyVL03A2RfWW6eKQlbvNyVarwDeuA6mHARuZ5k'
	print(url)
	http = urlopen(url)
	data = http.read().decode('utf-8')
	food_data_json = json.loads(data)
	nutrients = food_data_json['report']['food']['nutrients']
	calories = [nutrient for nutrient in nutrients if nutrient['name'] == 'Energy' and nutrient['unit'] == 'kcal']
	return calories

@app.route('/calories/<recipe_id>', methods=['GET'])
def calculate_calories(recipe_id):

	if recipe_id in results_cache:
		results = results_cache[recipe_id]
		return jsonify(**results)

	ingredients = frontrecipescraper.call_this(recipe_id) 
	print('\n\n\nasdf2', ingredients, type(ingredients), '\n\n\n')
	
	results = {}
	
	for _, ingredient in ingredients.items():
		print('asdf3', ingredient)
		usda_code, quantity, units_list, name = scraper.call_this(ingredient)
		if not quantity:
			continue
		quantity = float(quantity)
		if usda_code == -1:
			continue
		cal_dict = find_info(usda_code)
		calories = calculate_calories(cal_dict, quantity, units_list)
		
		results[name] = calories
	
	results['total']  = sum(results.values())	
	results_cache[recipe_id] = results	
			
	return jsonify(**results)

	
convert_to_grams = {
	'cup': 250,
	'cups': 250,
	'tsp': 5,
	'tablespoon': 15,
	'tablespoons': 15,
	'lbs': 453,
	'pound': 453,
	'pounds': 453,
	'kilograms': 1000,
	'kg': 1000,
	'ounce': 28,
	'oz': 28,
	'ounces': 28,
}

def calculate_calories(info, quantity, units_list):
	default_value = float(info[0]['value'])
	measures = info[0]['measures']
	for measure in measures:
		label = measure['label']
		for unit in units_list:
			if label in unit or unit in label:
				value = float(measure['value'])
				return quantity * value
	
	# need to convert to grams
	for conversion, factor in convert_to_grams.items():
		for unit in units_list:
			if conversion in unit:
				grams = factor * quantity
				return grams / 100 * default_value		
	
	return 0	

if __name__ == "__main__":
	app.run(debug=True)	
