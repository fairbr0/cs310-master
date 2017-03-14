$(document).ready(function () {
    $(".article-feed-area").masonry({
        itemSelector: '.post',
        isAnimated: true,
        columnWidth: function( containerWidth ) {

            var width = $(window).width();
            var col = 300;


            if(width < 1200 && width >= 980) {
                col = 240;
            }
            else if(width < 980 && width >= 768) {
                col = 186;
            }

            return col;
          }
    });

});
