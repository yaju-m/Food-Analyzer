document.addEventListener('DOMContentLoaded', function() {
    var checkPageButton = document.getElementById('checkPage');
  
    function isImage(i) {
        return i instanceof HTMLImageElement;
    }

    checkPageButton.addEventListener('click', function() {
        console.log('TEST TEST TEST');
        console.log(JSON.stringify($('.body-content')));
    }, false);
}, false);
