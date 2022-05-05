new Swiper('.cafe-image .swiper-container', {
    slidesPerView: 3,   //한번에 보여줄 슬라이드 개수
    spaceBetween: 10,   //슬라이드 사이 여백
    centeredSlides: true,
    loop: true,
    autoplay: {
        delay: 5000
    },
    navigation: {
        prevEl: '.cafe-image .swiper-prev',
        nextEl: '.cafe-image .swiper-next'
    }

});