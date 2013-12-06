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

    $('.icon-arrow-btn').click(function(){

        if($(this).hasClass('active')){
            $('.form-bot').fadeOut(100)
            $(this).removeClass('active');
            $('.fixed-contato').animate({"height": "35px"}, "fast");
            $('.fixed-contato').animate({"width": "222px"}, "fast");
        }else{
           $(this).addClass('active');
           $('.fixed-contato').animate({"height": "500px"}, "fast");
           $('.fixed-contato').animate({"width": "550px"}, "fast"); 

           setTimeout(function() {
                $('.form-bot').fadeIn(100)
           }, 500);
           
        }
    });


    var topArticle;
     //Define o tamanho da estrutura.
    $('.link-home').click(function () {
         topArticle = 0;
         $('html, body').stop().animate({
             scrollTop: topArticle
         }, 1000);
     });

    $('.link-produto').click(function () {
         topArticle = 1225;
         $('html, body').stop().animate({
             scrollTop: topArticle
         }, 1000);
     });

    $('.link-quem').click(function () {
         topArticle = 2960;
         $('html, body').stop().animate({
             scrollTop: topArticle
         }, 1000);
     });

    $('.link-contato').click(function () {
         topArticle = 4365;
         $('html, body').stop().animate({
             scrollTop: topArticle
         }, 1000);
     });

    // Menu active
    $('.menu ul li a').click(function(){
        $('.menu ul li a').removeClass('selected');
        $(this).addClass('selected');
    });

    $('.btn-carac').click(function(){
        topArticle = 80;
         $('html, body').stop().animate({
             scrollTop: topArticle
         }, 1000);
    });

    $(".fancybox-thumb").fancybox({
        width : 960,
        height : 800,
        afterShow: function(){
            $('.fancybox-inner').wrap(
                $('<a>')
                .attr('href', $(this.element).attr('href'))
                .addClass('cloud-zoom')
                .attr('rel', "position: 'inside'")
            );
            $('.cloud-zoom').CloudZoom();
        },  
        openEffect : 'none',
        closeEffect : 'none',
        prevEffect : 'none',
        nextEffect : 'none',
        arrows : true,
        helpers : {
            title : {
                type : 'inside'
            },
            thumbs : {
                width: 40,
                height: 40
            }
        }
    });

    setTimeout(function() {
          $('.destaque-description.well').animate({"margin-top": "30px"}, "fast");
    }, 500);
    

});