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
    gsap.to(window, .3, {
        scrollTo: 0
    });
});

const thisYear = document.querySelector('.this-year');
thisYear.textContent = new Date().getFullYear();

const headerMenu = document.querySelector('#sidebarToggle');
const sidebar = document.querySelector('.sidebar');
headerMenu.addEventListener('click', function(){
    if(!sidebar.classList.contains('active')){
        sidebar.classList.add('active')
    }
    else{
        sidebar.classList.remove('active')
    }
});

