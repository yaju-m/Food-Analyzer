var cheerio = require('cheerio');
var request = require('request');

request({
    method: 'GET',
    url: 'https://allrecipes.com/'
}, function(err, response, body) {
    if (err) return console.error(err);
    if (response) return console.log(response); 

    // Tell Cherrio to load the HTML
    $ = cheerio.load(body);
    $('h3.grid-col__h3 grid-col__h3--recipe-grid').each(function() {
            var href = $('a.href', this).attr('href');
            if (href.lastIndexOf('/') > 0) {
                console.log($('h3', this).text());
            }
    });
});
