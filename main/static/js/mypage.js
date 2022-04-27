// mypage profile image upload
const realUpload = document.querySelector('.real-upload');
const upload = document.querySelector('.upload');
// 파일이 이미지가 아니면 경고
upload.addEventListener('click', () => realUpload.click());


const reader = new FileReader();
reader.onload = (readerEvent) => {
    document.querySelector("#img_section1").setAttribute("src", readerEvent.target.result);
    //파일을 읽는 이벤트가 발생하면 img_section의 src 속성을 readerEvent의 결과물로 대체함
};

document.querySelector("#upload_file1").addEventListener("change", (changeEvent) => {
    //upload_file 에 이벤트리스너를 장착

    const imgFile = changeEvent.target.files[0];
    reader.readAsDataURL(imgFile);
    //업로드한 이미지의 URL을 reader에 등록
})

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


// sendbtn = document.getElementById('profile_send');
// sendbtn.addEventListener("click", function(){
//     param = {
//         'user_id':user_id,
//         'img':upload.src,
//         'csrfmiddlewaretoken': csrftoken,
//     }
//     $.ajax({
//         type: "POST",
//         url: 'userprofile/',
//         data: param,
//         success: function (data) {
//             console.log("success")
//         },
//         error: function (e) {
//             console.log("error", e);
//         }
//     })

// });