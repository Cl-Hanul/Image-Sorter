var didScroll;

var lastScrollTop = 0;
var delta = 20;
var startshow = 40;
var navbarheight = $('.Hanul-Scroll-header').outerHeight();

$(window).scroll(function(event){
    didScroll = true;
});

setInterval(function(){
    if (didScroll){
        hasScrolled();
        didScroll = false;
    }
})

function hasScrolled(){
    var st = $(this).scrollTop();
    var header = $('.Hanul-Scroll-header')

    if (st < startshow) {
        header.removeClass('nav-down').addClass('nav-up')
        return
    }

    if (Math.abs(lastScrollTop-st) <= delta)
        return

    if (st > lastScrollTop){
        header.removeClass('nav-down').addClass('nav-up')
    } else {
        if(st + $(window).height() < $(document).height()){
            header.removeClass('nav-up').addClass('nav-down')
        }
    }

    lastScrollTop = st;
}