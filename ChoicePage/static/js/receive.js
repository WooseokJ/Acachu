const receivedData = location.href.split('?')[1];

console.log(decodeURI(receivedData)); // 전달받은 데이터 한글