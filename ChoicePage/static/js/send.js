function test(url){ // 위치
  var send = document.cateory_form;
  send.action=url;
  send.method='post';
  send.submit();
}

function SendVal(val){
  var send = document.cateory_form;
  document.getElementById("category").value = val;
  send.action='/recommendlist/'
  send.method='post';
  send.submit();
}