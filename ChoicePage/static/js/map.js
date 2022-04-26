 // 지도를 표시할 div
 var mapContainer = document.getElementById('map'),
 mapOption = {
     center: new kakao
         .maps
         .LatLng( 37.35879, 127.11494), // 지도의 중심좌표
     level: 1 // 지도의 확대 레벨
 };

// 지도를 생성합니다
var map = new kakao.maps.Map(mapContainer, mapOption);

// 주소-좌표 변환 객체를 생성합니다
var geocoder = new kakao.maps.services.Geocoder();

// 지도 확대 축소를 제어할 수 있는  줌 컨트롤을 생성합니다
var zoomControl = new kakao.maps.ZoomControl();
map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT);

// 확대 축소
// 지도가 확대 또는 축소되면 마지막 파라미터로 넘어온 함수를 호출하도록 이벤트를 등록합니다
kakao.maps.event.addListener(map, 'zoom_changed', function() {        
 
 // 지도의 현재 레벨을 얻어옵니다
 var level = map.getLevel();
});

// 클릭시 위치 표시
// 마커표시
var marker = new kakao.maps.Marker(), // 클릭한 위치를 표시할 마커입니다
 infowindow = new kakao.maps.InfoWindow({zindex: 1}); // 클릭한 위치에 대한 주소를 표시할 인포윈도우입니다

// 지도를 클릭했을 때 클릭 위치 좌표에 대한 주소정보를 표시하도록 이벤트를 등록합니다
kakao.maps.event.addListener(map, 'click', function (mouseEvent) {
     searchDetailAddrFromCoords(mouseEvent.latLng, function (result, status) {
         Marker(mouseEvent.latLng,status,result);
     });
 });

// 현재 위치 표시
// 현재위치 추적 HTML5의 geolocation으로 사용할 수 있는지 확인합니다
if (navigator.geolocation) {
 // GeoLocation을 이용해서 접속 위치를 얻어옵니다
 navigator.geolocation.getCurrentPosition(function (position) {
         var lat = position.coords.latitude, // 위도
             lon = position.coords.longitude; // 경도

         var locPosition = new kakao.maps.LatLng(lat, lon) // 마커가 표시될 위치를 geolocation으로 얻어온 좌표로 생성합니다

         searchDetailAddrFromCoords(locPosition, function (result, status) {
             Marker(locPosition,status,result);
         });
     });
} else { // HTML5의 GeoLocation을 사용할 수 없을때 마커 표시 위치와 인포윈도우 내용을 설정합니다

 var locPosition = new kakao.maps.LatLng(33.450701, 126.570667), message = 'geolocation을 사용할수 없어요'

 // 마커를 클릭한 위치에 표시합니다
 marker.setPosition(locPosition);
 marker.setMap(map);
 map.setCenter(locPosition);

 // 인포윈도우에 메시지 표시
 infowindow.setContent(message );
 infowindow.open(map, marker);
}

// 좌표로 법정동 상세 주소 정보를 요청합니다
function searchDetailAddrFromCoords(coords, callback) {
 geocoder.coord2Address(coords.getLng(), coords.getLat(), callback);
}

// 지도에 마커와 인포윈도우를 표시하는 함수입니다
function Marker(locPosition,status,result){
 if (status === kakao.maps.services.Status.OK) {
     var nowAddr = !!result[0].road_address ? result[0].road_address.address_name : result[0].address.address_name;
     var lotAddr = result[0].address.address_name;
     var detailAddr = !!result[0].road_address ? '<div>도로명주소 : ' + result[0].road_address.address_name + '</div>': '';
     detailAddr += '<div>지번 주소 : ' + result[0].address.address_name + '</div>';

     var content = '<div class="bAddr"><span style="font-weight:bold;">현재 위치</span>' + detailAddr + '</div>';

     // 마커를 클릭한 위치에 표시합니다
     marker.setPosition(locPosition);
     marker.setMap(map);
     map.setCenter(locPosition);

     // 인포윈도우에 클릭한 위치에 대한 법정동 상세 주소정보를 표시합니다
     infowindow.setContent(content);
     infowindow.open(map, marker);
     
     var addr = lotAddr.split(' ');
     if(addr[2].charAt(addr[2].length-1) !='구'){
        document.getElementById("sido").value = addr[0]; // 시도
        document.getElementById("sigg").value = addr[1]; // 시군구
        document.getElementById("emdong").value = addr[2]; // 읍면동
     }
     else{ // ex) 경기 성남시 분당구 정자동 -> 경기 / 성남시 분당구 / 정자동
        document.getElementById("sido").value = addr[0]; // 시도
        document.getElementById("sigg").value = addr[1]+' '+addr[2]; // 시군구
        document.getElementById("emdong").value = addr[3]; // 읍면동
     }

     document.getElementById("road_address").value = nowAddr; // 입력값에 넣을 현재위치
     document.getElementById("address_now").text = nowAddr; // 현재 위치에 주소 넣기

     

     // 현재 위치 값 null이면 none null 아니면 block
     window.scrollTo(0,400)
     $("#category_id").show();
 }
}

window.onload = function(){
 document.getElementById("address_btn").addEventListener("click", function(){ //버튼 클릭하면
     //카카오 지도 발생
     new daum.Postcode({
         oncomplete: function(data) { //선택시 입력값 세팅

            var addr = data.address.split(' ');
            if(addr[2].charAt(addr[2].length-1) !='구'){
                document.getElementById("sido").value = addr[0]; // 시도
                document.getElementById("sigg").value = addr[1]; // 시군구
                document.getElementById("emdong").value = addr[2]; // 읍면동
            }
            else{ // ex) 경기 성남시 분당구 정자동 -> 경기 / 성남시 분당구 / 정자동
                document.getElementById("sido").value = addr[0]; // 시도
                document.getElementById("sigg").value = addr[1]+' '+addr[2]; // 시군구
                document.getElementById("emdong").value = addr[3]; // 읍면동
            }

            document.getElementById("road_address").value = data.address; // 입력값에 넣을 현재위치
            document.getElementById("address_now").text = data.address; // 현재 위치에 주소 넣기

             // 검색 위치 지도 마커 표시
            geocoder.addressSearch(data.address, function(result, status) { // 주소입력 검색
                 // 정상적으로 검색이 완료됐으면
                 if (status === kakao.maps.services.Status.OK) {
                     var locPosition = new kakao.maps.LatLng(result[0].y, result[0].x);
                     Marker(locPosition , status,result);
                 }
                 else if (status === kakao.maps.services.Status.ZERO_RESULT) {
                     alert('검색 결과가 존재하지 않습니다.');
                     return;
                 }
            });
         }
     }).open();
 });
}