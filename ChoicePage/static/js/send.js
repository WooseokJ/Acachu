function test(url){ // 위치
  var send = document.cateory_form;
  send.action=url;
  send.method='post';
  send.submit();
}

function SendVal(val){
  var send = document.cateory_form;
  document.getElementById("category").value = val;
  send.action='/recommendlist/'
  send.method='post';
  send.submit();
}

// $(document).ready(function () {
//     $("#imgsubmit").click(function () {
//         var tmp = $('#imageform');
//         var formData = new FormData(tmp[0]);
//         formData.append('upload_file1', $('input[type=file]')[0].files[0]);
//         var maskHeight = $(document).height();
//         var maskWidth  = window.document.body.clientWidth;
//         var mask       ="<div id='mask' style='position:absolute; z-index:9000; background-color:#000000; display:none; left:0; top:0;'></div>";
//         var loadingImg ='';
//         loadingImg +=" <div id='loadingImg' style='position:fixed; z-index:9500; display:block;'>";
//         loadingImg +=" <img src="+ gif +" />";
//         loadingImg += "</div>";  
//         $.ajax({
//             url: imageurl,
//             type: 'POST',
//             data: formData,
//             processData: false,
//             contentType: false,
//             async: false,
//             success: function (data) {

//             },
//             beforeSend: function () {
//                 $("body").append(mask);
//                 $('#mask').css({
//                     'width' : maskWidth,
//                     'height': maskHeight,
//                     'opacity' :'0.3'
//                 });
//                 $('#mask').show();
//                 $('body').append(loadingImg);
//                 $('#loadingImg').css({
//                   'opacity' :'1',
//                   'margin' : '0 auto',
//                   'left' : '50%',
//                   'top' : '50%',
//                   'transform' : 'translate(-50%,-50%)'
//               });
//                 $('#loadingImg').show();
//             },
//             complete: function () {
//                 $('#mask, #loadingImg').hide();
//                 $('#mask, #loadingImg').remove(); 
//             },
//         });
//     });
// });


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
  
  
  