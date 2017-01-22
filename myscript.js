//var URL = 'http://localhost:3000/';
var URL = 'http://107.170.77.233:3000/';

//debugger;
console.log('TEST TEST TEST');
//$('.body-content').css('background-color', 'yellow');

$('article.grid-col--fixed-tiles').css({"border-color": "red", "border-weight":"5px", "border-style":"solid"});

var parsedItems = [];

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

for (var i=0; i<parsedItems.length; i++) {
    var element = parsedItems[i].element;
    var id = parsedItems[i].recipeId;
    element.hover(
        function() {
            // mouse enter
             
            var xhr = new XMLHttpRequest();
            xhr.open('GET', URL+'calculate/'+id, true);
            xhr.onload = function() {
                if (xhr.readyState == 4) {
                    console.log(xhr.responseText);           
                    element.before('<div id="'+id+'"><p>'+xhr.responseText+'</p></div>');
                }
            };
            xhr.send();
        }, function() {
            // mouse exit
            //$('#'+id).remove();
            console.log('Mouse moved away from me now I am sad :(');
        }
    );
}

/*
var processedItems = parsedItems.filter(function(item) {
    
    console.log('Sending requests for ' + item.recipeId);

    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://localhost:3000/calculate/'+item.recipeId, true);
    xhr.onload = function() {
        if (xhr.readyState == 4) {
            
            console.log(xhr.responseText);
        }
    }
    xhr.send();    
});

console.log('done');*/ 
