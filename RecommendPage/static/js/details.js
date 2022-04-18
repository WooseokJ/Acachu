new Swiper('.cafe-image .inner .swiper-container', {
    slidesPerView: 1,   //한번에 보여줄 슬라이드 개수
    spaceBetween: 100,   //슬라이드 사이 여백
    centeredSlides: true,
    loop: true,
    autoplay: {
        delay: 3000
    },
    navigation: {
        prevEl: '.cafe-image .inner .swiper-prev',
        nextEl: '.cafe-image .inner .swiper-next'
    }

});