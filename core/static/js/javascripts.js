jQuery(function(){

    // Click scroll
    $("a[data-scroll]").click(function(){
        $("html,body").animate(
            { scrollTop: $("." + $(this).data("scroll")).position().top },
            1000
        );
    });

    // Define o tamanho
    function updateSize() {
        $("html").width($(window).width());
    };

    updateSize;

    $(window).resize(
        updateSize
    );

    // Parallax
    //mseg = $(".caracteristicas").position().top;
    //mter = $(".clientes").position().top;

    function Move(){

        var pos = $(window).scrollTop();

        $(".destaque-photo").css({
            'top': -pos / 2
        });

       /* if (pos >= 0) {
            $(".menu li.selected").removeClass();
            $(".menu a[data-scroll='topo']").parent().addClass("selected");
        }
        if (pos >= mseg) {
            $(".menu li.selected").removeClass();
            $(".menu a[data-scroll='caracteristicas']").parent().addClass("selected");
        }
        if (pos >= mter) {
            $(".menu li.selected").removeClass();
            $(".menu a[data-scroll='clientes']").parent().addClass("selected");
        } */

    }

    $(window).bind('scroll', function(){
        Move();
    });

});