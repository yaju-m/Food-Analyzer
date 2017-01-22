var URL = 'http://localhost:5000/';
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

//for (var i=0; i<parsedItems.length; i++) {
//    var element = parsedItems[i].element;
//    var id = parsedItems[i].recipeId;
//    var xhr = new XMLHttpRequest();
//    xhr.open('GET', URL+'calories/'+id, true);
//    xhr.onload = function() {
//        if (xhr.readyState == 4) {
//            response = JSON.parse(xhr.responseText);
//            element.before(
//                '<div id="'+id+'"' +
//                    '<p>'+response.total+'</p>' +
//                '</div>'
//            );
//            element.hover(function() {
//                $('.hover-info').remove();
//                $('#'+id).append(
//                    '<div id="'+id+'extra" class="hover-info">' +
//                        '<p>'+response+'</p>' +
//                    '</div>'
//                );
//            }, function() {
//                $('#'+id+'extra').remove();
//            });
//        }    
//    }
//    xhr.send();        
//}

var hovering = false;
var doneLoading = true;

// Add hover thingy for each valid tile
for (var i=0; i<parsedItems.length; i++) {
  var element = parsedItems[i].element;
  var id = parsedItems[i].recipeId;
  element.hover(
    function(element, id) {
      return function() {
        // mouse enter
        hovering = true;
        doneLoading = false;
        $('.hover-info').remove();
        element.before(
          // TODO Add styling
          '<div id="'+id+'" class="hover-info">' + 
            '<p id="'+id+'-loading" class="fade">Placeholder...</p>' +
          '</div>'
        );
        loadingP = $('#'+id+'-loading');
        console.log('Loading stuff into:' + loadingP);
        showLoadingText(loadingP, 0);

        var xhr = new XMLHttpRequest();
        xhr.open('GET', URL+'calories/'+id, true);
        xhr.onload = function() {
          if (xhr.readyState == 4) {
            doneLoading = true;
            loadingP.removeClass('fade');
            loadingP.remove();
            console.log(xhr.responseText);
            $('#'+id).append(
              '<ul id="'+id+'-list" class="collection"></ul>'
            );
            results = JSON.parse(xhr.responseText);
            $('#'+id+'-list').append(
              '<li class="collection-item">Total: '+results.total+' Cal</li>'
            );
            $.each(results, function(k, v) {
              //display the key and value pair
              if (k != 'total') {
                $('#'+id+'-list').append(
                  '<li class="collection-item">'+k+': '+v+' Cal</li>'
                );
              }
            });
          }
        };
        xhr.send();
      }
    }(element, id), 
    function(element, id) {
      return function() {
        // mouse exit
        hovering = false;
        $('#'+id).remove();
        console.log('Mouse moved away from me now I am sad :(');
      }
    }(element, id)
  );
}

var loadingTextIdx = 0;
var loadingTextList = [
  'Calculating...',
  'Consulting Google overlords...',
  'Decoding natural languages...',
  'Eating our veggies...',
];
function showLoadingText(element) {
  if (hovering && !doneLoading) {
    console.log(loadingTextList[loadingTextIdx]);
    element.html(loadingTextList[loadingTextIdx]);
    setTimeout(function() {
      loadingTextIdx = (loadingTextIdx+1)%loadingTextList.length;
      showLoadingText(element);
    }, 3000);
  }
}
