window.addEventListener('hashchange', function(){
    var hash = window.location.hash;
    var imageId = hash.split('=')[1];
    var image = this.document.getElementById('main-image-img');
    console.log(imageId);
    var vv = 335/image.offsetHeight;
    image.setAttribute('src',"../static/images/"+imageId);
    image.setAttribute('style',"width:"+image.offsetWidth*vv+";");
    image.setAttribute('height',335);
});