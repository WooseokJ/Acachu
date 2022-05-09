$(document).ready(function () {
    $("#imageform").submit(function () {
        var maskHeight = $(document).height();
        var maskWidth  = window.document.body.clientWidth;
        var mask       ="<div id='mask' style='position:absolute; z-index:9000; background-color:#000000; display:none; left:0; top:0;'></div>";
        var loadingImg ='';
        loadingImg +=" <div id='loadingImg' style='position:fixed; z-index:9500; display:block;'>";
        loadingImg +=" <img src="+ gif +" />";
        loadingImg += "</div>";  

        $("body").append(mask);
        $('#mask').css({
            'width' : maskWidth,
            'height': maskHeight,
            'opacity' :'0.3'
        });
        $('#mask').show();
        $('body').append(loadingImg);
        $('#loadingImg').css({
        'opacity' :'1',
        'margin' : '0 auto',
        'left' : '50%',
        'top' : '50%',
        'transform' : 'translate(-50%,-50%)'
        });
        $('#loadingImg').show();
    });
});
  