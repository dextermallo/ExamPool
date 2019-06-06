$( document ).ready(function() {
    $(".ql-editor").focus(function(){
        $("#editor-container").css("box-shadow", "rgb(50, 132, 255) 0px 0px 10px");
        $(".corner").css("transform", "translate(7px, 7px)");
        $(".corner").css("z-index", "-1");
        $(".corner-r").css("transform", "translate(-7px, -7px) scale(-1,-1)");
        $(".corner-r").css("z-index", "-1");
    });
    $(".ql-editor").focusout(function(){
        $("#editor-container").css("box-shadow", "none");
        $(".corner").css("transform", "translate(0px, 0px)");
        $(".corner").css("z-index", "1");
        $(".corner-r").css("transform", "translate(0px, 0px) scale(-1,-1)");
        $(".corner-r").css("z-index", "1");
    });
});