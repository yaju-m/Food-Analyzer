var express = require('express');
var cheerio = require('cheerio');
var app = express();

app.get('/', function(req, res) {
    res.send('Hello World!');
});

app.get('/calculate/:recipeId', function(req, res) {
    var url = 'http://allrecipes.com/recipe/'+req.params.recipeId;
    request(url, function (error, response, body) {
        if (!error && response.statusCode == 200) {
            console.log(body);
        }
    })
});

app.listen(3000, function() {
    console.log('App listening on port 3000!');
});
