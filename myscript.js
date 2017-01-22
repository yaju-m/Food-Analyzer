var URL = 'http://localhost:3000/';
//var URL = 'http://107.170.77.233:3000/';

console.log('TEST TEST TEST');

// This will be an array of all the tiles that link to valid recipes
var parsedItems = [];

// Iterate through every tile and determine which link to valid recipes
$('article.grid-col--fixed-tiles').each(function() {
    var gridItem = $(this);
    var id = "";
    $(this).find('a[href^="/recipe/"]').each(function() {
        var url = $(this).attr('href');
        id = url.split('/')[2];
    });
    if (id) {
        parsedItems.push({
            element: gridItem,
            recipeId: id
        });
    }
});

// Add hover thingy for each valid tile
for (var i=0; i<parsedItems.length; i++) {
    var element = parsedItems[i].element;
    var id = parsedItems[i].recipeId;
    element.hover(
        function(element, id) {
            return function() {
                // mouse enter
                var xhr = new XMLHttpRequest();
                xhr.open('GET', URL+'calculate/'+id, true);
                xhr.onload = function() {
                    if (xhr.readyState == 4) {
                        console.log(xhr.responseText);
                        $('.hover-info').remove();           
                        element.before(
                            // TODO Add styling
                            '<div id="'+id+'" class="hover-info">' + 
                                '<p>'+xhr.responseText+'</p>' +
                            '</div>'
                        );
                    }
                };
                xhr.send();
            }
        }(element, id), 
        function(element, id) {
            return function() {
                // mouse exit
                $('#'+id).remove();
                console.log('Mouse moved away from me now I am sad :(');
            }
        }(element, id)
    );
}
