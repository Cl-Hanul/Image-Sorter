function mousemove(event){
    var menu_ui = $('.Hanul-Toggle-secter');

    if (event.pageX < 40){
        menu_ui.removeClass('hide-menu').addClass('show-menu');
    }
    if (event.pageX > 130){
        menu_ui.removeClass('show-menu').addClass('hide-menu');
    }

};

window.addEventListener('mousemove',mousemove)