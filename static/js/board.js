$( document ).ready(function() {
    var goto_open = false;
    $(".show-goto").click(function(){
        if(goto_open == false){
            $(".goto-wrapper").css("animation-name", "page-goto-animation");
            goto_open = true;
        }
        else{
            $(".goto-wrapper").css("animation-name", "page-goto-animation-backword");
            goto_open = false;
        }
    });

    $(".arrow").hover(
        function(){
            $(this).find(".page-hover-stick-left").css("animation-name", "page-hover-stick-left-animation");
            $(this).find(".page-hover-stick-right").css("animation-name", "page-hover-stick-right-animation");
        },
        function(){
            $(this).find(".page-hover-stick-left").css("animation-name", "none");
            $(this).find(".page-hover-stick-right").css("animation-name", "none");
        }
    );
});