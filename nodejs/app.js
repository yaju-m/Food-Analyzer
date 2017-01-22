var express = require('express');
var app = express();

app.get('/', function(req, res) {
    res.send('Hello World!');
});

app.get('/calculate/:recipeId', function(req, res) {
    res.send({
        calories: req.params.recipeId
    });
});

app.listen(3000, function() {
    console.log('App listening on port 3000!');
});
