var mapContainer = document.getElementById('map'), // 지도를 표시할 div
    mapOption = {
        center: new kakao
            .maps
            .LatLng(33.450701, 126.570667), // 지도의 중심좌표
        level: 1 // 지도의 확대 레벨
    };

// 지도를 생성합니다
var map = new kakao
    .maps
    .Map(mapContainer, mapOption);

// 주소-좌표 변환 객체를 생성합니다
var geocoder = new kakao
    .maps
    .services
    .Geocoder();

var marker = new kakao
        .maps
        .Marker(), // 클릭한 위치를 표시할 마커입니다
    infowindow = new kakao
        .maps
        .InfoWindow({zindex: 1}); // 클릭한 위치에 대한 주소를 표시할 인포윈도우입니다

// 지도를 클릭했을 때 클릭 위치 좌표에 대한 주소정보를 표시하도록 이벤트를 등록합니다
kakao
    .maps
    .event
    .addListener(map, 'click', function (mouseEvent) {
        searchDetailAddrFromCoords(mouseEvent.latLng, function (result, status) {
            if (status === kakao.maps.services.Status.OK) {
                var detailAddr = !!result[0].road_address
                    ? '<div>도로명주소 : ' + result[0].road_address.address_name + '</div>'
                    : '';
                detailAddr += '<div>지번 주소 : ' + result[0].address.address_name + '</div>';

                var content = '<div class="bAddr">' + detailAddr + '</div>';

                // 마커를 클릭한 위치에 표시합니다
                marker.setPosition(mouseEvent.latLng);
                marker.setMap(map);

                // 인포윈도우에 클릭한 위치에 대한 법정동 상세 주소정보를 표시합니다
                infowindow.setContent(content);
                infowindow.open(map, marker);
            }
        });
    });

function searchDetailAddrFromCoords(coords, callback) {
    // 좌표로 법정동 상세 주소 정보를 요청합니다
    geocoder.coord2Address(coords.getLng(), coords.getLat(), callback);
}

// 현재위치 추적 HTML5의 geolocation으로 사용할 수 있는지 확인합니다
if (navigator.geolocation) {
    // GeoLocation을 이용해서 접속 위치를 얻어옵니다
    navigator
        .geolocation
        .getCurrentPosition(function (position) {

            var lat = position.coords.latitude, // 위도
                lon = position.coords.longitude; // 경도

            var locPosition = new kakao
                    .maps
                    .LatLng(lat, lon), // 마커가 표시될 위치를 geolocation으로 얻어온 좌표로 생성합니다
                message = '<div style="width:150px;text-align:center;padding:6px;">현재 위치</div>'; // 인포윈도우에 표시될 내용입니다

                searchDetailAddrFromCoords(locPosition, function (result, status) {
                    if (status === kakao.maps.services.Status.OK) {
                        var detailAddr = !!result[0].road_address
                            ? '<div>도로명주소 : ' + result[0].road_address.address_name + '</div>'
                            : '';
                        detailAddr += '<div>지번 주소 : ' + result[0].address.address_name + '</div>';
        
                        var content = '<div class="bAddr">' + detailAddr + '</div>';
                        // 마커와 인포윈도우를 표시합니다
                         displayMarker(locPosition, content);
                    }
                });

            
        });

} else { // HTML5의 GeoLocation을 사용할 수 없을때 마커 표시 위치와 인포윈도우 내용을 설정합니다

    var locPosition = new kakao
            .maps
            .LatLng(33.450701, 126.570667),
        message = 'geolocation을 사용할수 없어요'

    displayMarker(locPosition, message);
}

// 지도에 마커와 인포윈도우를 표시하는 함수입니다
function displayMarker(locPosition, message) {

    // 마커를 생성합니다
    var marker = new kakao
        .maps
        .Marker({map: map, position: locPosition});

    var iwContent = message, // 인포윈도우에 표시할 내용
        iwRemoveable = true;

    // 인포윈도우를 생성합니다
    var infowindow = new kakao
        .maps
        .InfoWindow({content: iwContent});

    // 인포윈도우를 마커위에 표시합니다
    infowindow.open(map, marker);

    // 지도 중심좌표를 접속위치로 변경합니다
    map.setCenter(locPosition);
}

/*
        // 위치 검색하고 싶을때
        $('#searchBtn').click(function(){

            // 주소-좌표 변환 객체를 생성합니다
            var geocoder = new kakao.maps.services.Geocoder();

            // 주소로 좌표를 검색합니다
            geocoder.addressSearch($('#address').val(), function(result, status) { // 주소입력 검색

                // 정상적으로 검색이 완료됐으면
                if (status === kakao.maps.services.Status.OK) {
                    var locPosition = new kakao.maps.LatLng(result[0].y, result[0].x);
                    message = '<div style="width:150px;text-align:center;padding:6px;">찾는 위치</div>';
                    displayMarker(locPosition, message)
                }
            });
        });
        */
