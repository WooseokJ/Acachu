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