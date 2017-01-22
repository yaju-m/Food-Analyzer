# Food-App-FrontEnd

Food Analyzer is a Chrome extension that uses Machine Learning and Natural Language Processing to instantaneously obtain relevant nutritional information for recipes and ingredients seen online.

There were multiple parts during the development of this project. One of the main parts was the Chrome Extension that would continuously run in the background and analyze the contents of the recipes seen online. This was done through a web scraper that would aggregate information like the calorie count from the USDA Food Composition Database. In order to link the Chrome extension with the information gathered from the web scraper, we used the Natural Language Processing API from the Google Cloud Platform to analyze and categorize the relevant nutritional information.

To develop this extension, we used HTML/CSS/Javascript, Flask, jquery, the Google Cloud Platform's Natural Language Processing API, Beautiful-Soup, Scrapy, and Cheerio
