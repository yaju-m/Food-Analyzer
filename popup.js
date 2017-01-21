document.addEventListener('DOMContentLoaded', function() {
  var checkPageButton = document.getElementById('checkPage');
  
  function isImage(i) {
    return i instanceof HTMLImageElement;
  }

  checkPageButton.addEventListener('click', function() {

    /*chrome.tabs.getSelected(null, function(tab) {
          var x = event.clientX;  
          var y = event.clientY;

          window.alert(x);
          window.alert(y);
    });*/

          var x = event.clientX;  
          var y = event.clientY;

          window.alert(x);
          window.alert(y);
    
/*
    var x = event.clientX;  
    var y = event.clientY; 

    window.alert("xcoordinate:" + x);*/

  }, false);
}, false);