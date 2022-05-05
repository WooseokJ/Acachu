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

var textCount = document.querySelector('.textCount'); 

var review_wc = document.getElementById('review_wc');
review_wc.addEventListener('keyup', event =>{
    var count = review_wc.value.length;
    textCount.innerHTML = count;
});

new Swiper('.cafe-image .swiper-container', {
    slidesPerView: 3,   //한번에 보여줄 슬라이드 개수
    spaceBetween: 30,   //슬라이드 사이 여백
    centeredSlides: true,
    loop: false,
    navigation: {
        prevEl: '.inner .cafe-image .swiper-prev',
        nextEl: '.inner .cafe-image .swiper-next'
    }

});

const prevbtn = document.querySelector('.arrows .swiper-prev');
const nextbtn = document.querySelector('.arrows .swiper-next');
const currentcnt = document.querySelector('.cnts .current-cnt')
const totalcnt = document.querySelector('.cnts .total-cnt')
prevbtn.addEventListener('click', function(){
    if(parseInt(currentcnt.innerHTML) != 1)
    currentcnt.innerHTML -= 1;
    
});

nextbtn.addEventListener('click', function(){
    if(parseInt(currentcnt.innerHTML) < parseInt(totalcnt.innerHTML))
        currentcnt.innerHTML = parseInt(currentcnt.innerHTML) + 1;
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

