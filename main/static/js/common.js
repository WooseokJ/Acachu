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

// 사이드바 메뉴
// const headerMenu = document.querySelector('#sidebarToggle');
// const sidebar = document.querySelector('.sidebar');
// headerMenu.addEventListener('click', function(){
//     if(!sidebar.classList.contains('active')){
//         sidebar.classList.add('active')
//     }
//     else{
//         sidebar.classList.remove('active')
//     }
// });

function getCookie(name) { 
    var cookieValue = null; 
    if (document.cookie && document.cookie !== '') {
         var cookies = document.cookie.split(';'); 
        for (var i = 0; i < cookies.length; i++) { 
             var cookie = cookies[i].trim(); // Does this cookie string begin with the name we want? 
            if (cookie.substring(0, name.length + 1) === (name + '=')) { 
                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1)); 
                 break; 
            } 
        } 
    } 
    
    return cookieValue; 
} 

var csrftoken = getCookie('csrftoken');

const loginbtn = document.getElementById('login_btn')

loginbtn.addEventListener('click', function(){
    account = document.getElementById('login_id').value
    password = document.getElementById('login_pw').value
    param = {
        'user_account':account,
        'user_password':password,
        'csrfmiddlewaretoken': csrftoken,
    }
    $.ajax({
        type: "POST",
        url: 'logout',
        data: JSON.stringify(param),
        success: function (data) {
            console.log("success")
        },
        error: function (e) {
            console.log("error", e);
        }
    });
})

// const signupbtn = document.getElementById('signup_btn')
// loginbtn.addEventListener('click', function(){
//     param = {
//         'csrfmiddlewaretoken': csrftoken,
//     }
//     $.ajax({
//         type: "POST",
//         url: 'logout',
//         data: JSON.stringify(param),
//         success: function (data) {
//             console.log("success")
//         },
//         error: function (e) {
//             console.log("error", e);
//         }
//     });
// })
