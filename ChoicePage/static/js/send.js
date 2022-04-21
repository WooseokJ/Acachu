var address;

// 주소 검색
function search_cat(){
    address = document.getElementById("address_now").text;
    location.href = `category?${address}`;
}

function search_img(){
    address = document.getElementById("address_now").text;
    console.log(address); // 주소 값

    location.href = `imagesearch?${address}`;
}

function test(tt){
  console.log(address); // 주소 값
  //location.href = `/../recommendlist/?${tt+address}`;
  //window.location.href = `/./choice/imagesearch?${tt+'/'+address}`; // test
}