const toTopEl = document.querySelector('#to-top');

window.addEventListener('scroll', _.throttle(function(){
    console.log(window.scrollY);
    if(window.scrollY > 500){
        gsap.to(toTopEl, .2, {
            x: -150
        });

    } else {
        gsap.to(toTopEl, .2, {
            x: 150
        });

    }
}, 300));

toTopEl.addEventListener('click', function(){
    gsap.to(window, .7, {
        scrollTo: 0
    });
});

const thisYear = document.querySelector('.this-year');
thisYear.textContent = new Date().getFullYear();

