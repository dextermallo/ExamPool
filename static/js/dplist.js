$( document ).ready(function() {
    $(".card").hover(function(){
        $(this).css("z-index", "5");
        $(this).find(".card-img-top").css("transform", "scale(1.05)");
        //$(this).find(".card-divider").css("opacity", "1");
        //$(this).find(".card-text").css("opacity", "1");
        $(this).find(".card-body").css("max-height", "15rem");
        $(this).find(".card-divider").fadeIn();
        $(this).find(".card-text").css("opacity", "1");
        $(this).find(".card-text").fadeIn();
        $(this).find(".card-title").addClass("glitch");
    },function(){
        $(this).find(".card-img-top").css("transform", "scale(1)");
        //$(this).find(".card-divider").css("opacity", "0");
        //$(this).find(".card-text").css("opacity", "0");
        $(this).find(".card-body").css("max-height", "4rem");
        $(this).find(".card-divider").fadeOut();
        $(this).find(".card-text").fadeOut();
        $(this).find(".card-text").css("opacity", "0");
        $(this).find(".card-title").removeClass("glitch");
    });

    $(".card-img-container").hover(function(){
        $(this).find(".enter-img").css("opacity", "1");
        $(this).find(".card-img-top").css("filter", "grayscale(1)");
    },function(){
        $(this).find(".enter-img").css("opacity", "0");
        $(this).find(".card-img-top").css("filter", "grayscale(0)");
    });
});