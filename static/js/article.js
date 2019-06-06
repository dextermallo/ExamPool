$( document ).ready(function() {
    //$(".article-container").css("opacity", 1);
    //var article_height = $(".article-content").css("height");
    $(".article-content-container").each(function(){

        $(this).css("height", $(this).find(".article-content").css("height"));
    });
    //$(".article-content-container").fadeIn(500);
    $(".author-container").css("opacity", 1);;
    //$(".author-info-container").fadeIn(500);
    $('.author-info-block').each(function(index){
        $(this).css("top",  index * 50 + "px");
        $(this).delay(index * 200 + 200).fadeIn(1000);
    });
    $(".user-avatar").fadeIn(1000);
    $(".user-name").delay(200).fadeIn(1000);
});