$('#mapbtn').click(function(){
    var offset = $('#location').offset();
    offset.top -= 200;
    $('html').animate({scrollTop : offset.top}, 100);
});

$('#imagebtn').click(function(){
    var offset = $('#cafeimage').offset();
    offset.top -= 200;
    $('html').animate({scrollTop : offset.top}, 100);
});

$('#reviewbtn').click(function(){
    var offset = $('#review').offset();
    offset.top -= 200;
    $('html').animate({scrollTop : offset.top}, 100);
});


new Swiper('.cafe-image .swiper-container', {
    slidesPerView: 1,   //한번에 보여줄 슬라이드 개수
    spaceBetween: 50,   //슬라이드 사이 여백
    centeredSlides: true,
    loop: true,
    autoplay: {
        delay: 5000
    },
    navigation: {
        prevEl: '.cafe-image .inner .swiper-prev',
        nextEl: '.cafe-image .inner .swiper-next'
    }

});

const bookmark = document.querySelector('.bookmark')

bookmark.addEventListener('click', function(){
    let param ={
        'store_id' : store_id,
        'user_id' : user_id,
    }
    if(!bookmark.classList.contains('active')){
        bookmark.classList.add('active');
        $.ajax({
            url: reg_url,
            type: 'POST',
            data: JSON.stringify(param),
            success:function(data){
                console.log(data);
            },
            error: function(){
                alert('즐겨찾기 등록 도중에 에러가 발생했습니다');
            }
        });
    }
    else{
        bookmark.classList.remove('active');
        $.ajax({
            url: del_url,
            type: 'POST',
            data: JSON.stringify(param),
            success:function(data){
                console.log(data);
            },
            error: function(){
                alert('즐겨찾기 등록 도중에 에러가 발생했습니다');
            }
        });
    }
});

document.querySelector('#reviewForm input[name=store]').value = store_id
document.querySelector('#reviewForm input[name=user]').value = user_id

