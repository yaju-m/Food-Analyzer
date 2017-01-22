# Food-App-FrontEnd

Food Analyzer is a Chrome extension that uses machine learning and natural language processing to instantaneously obtain relevant nutritional information for recipes found online.

![alt text](https://github.com/yaju-m/Food-App-FrontEnd/blob/master/FoodAnalyzer2.png "Example of Chrome Browser Extension")

The development of our project involved a variety of technologies. One of the main parts was a Chrome Extension that would continuously analyze the contents of recipes seen online. This was done through a web scraper that would aggregate nutritional information from the USDA's Food Composition Database. In order to link the Chrome extension with nutritional information, we wrote another web scraper to extract from the ingredient list and used the Google Cloud Platform's Natural Language Processing API to analyze and categorize information in the recipe to generate specific calorie counts for each ingredient.

To develop this extension, we used HTML/CSS/Javascript, Flask, JQuery, the Google Cloud Platform's Natural Language Processing API, Beautiful-Soup, Scrapy, and Cheerio
