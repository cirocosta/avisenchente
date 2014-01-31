geocoder = null;
map = null;
LATLNG_ADDRESS = null;
allMarkers = [];

/* Inicializa o mapa com configuracoes pre-definidas */

function initialize() {
    var mapOptions = {
        center: new google.maps.LatLng(-23.5489433, -46.6388182),
        zoom:12,
        zoomControl: true,
        panControl: false,
        mapTypeControl: false,
        scaleControl: false,
        streetViewControl: false,
        overviewMapControl: false,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };

  /* Atribui variavel map globalmente */

  map = new google.maps.Map(document.getElementById("map-canvas"),
    mapOptions);

  /* Atribui variavel geocoder globalmente */

  geocoder = new google.maps.Geocoder();

}

/* Converte um objeto LatLng para um endereco em forma de string */

function codeLatLng(geocoder, latlng, id_endereco){
  geocoder.geocode({'latLng': latlng}, function(results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
      if (results[0]) {
          var end = document.getElementById(id_endereco);
          end.value = results[0].formatted_address;
      } else {
        return false;
      }
    } else {
      return false;
    }
  });
}

/* Converte um endereco em formato de String para um objeto LatLng */

function codeAddress(geocoder, endereco, mapa) {
  geocoder.geocode({
    'address':endereco
  }, function(results,status) {
    if(status == google.maps.GeocoderStatus.OK) {
      var position = results[0].geometry.location;
      putMarker(map, position);
      LATLNG_ADDRESS = position;
      console.log(position.toString());
    }
    return false;
  });
}

/*  Adiciona um marcador no mapa dada uma posicao.
    Requer a lista global de marcadores allMarkers definida.
 */

function putMarker(mapa, posicao){
    window.setTimeout(function(){
      mapa.panTo(posicao);
      mapa.setZoom(14);
    },400)
    if(allMarkers.length > 0){
      allMarkers[0].setMap(null);
      allMarkers.pop();
    }
    var marker = new google.maps.Marker({
      map:mapa,
      animation: google.maps.Animation.DROP,
      draggable:true,
      title:"Mova-me!",
      position:posicao
    });
    google.maps.event.addListener(marker,'dragend',function(){
      allMarkers[0] = marker.getPosition();
    });
    google.maps.event.addListener(marker,'click',function(){
      map.panTo(marker.getPosition());
      infowindow.open(mapa,marker);
    });
    allMarkers.push(marker);
}

/* Apos o carregamento do corpo do documento, executa a funcao
initialize definida acima */

google.maps.event.addDomListener(window, 'load', initialize);