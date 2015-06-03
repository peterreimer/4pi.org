/*function getLatLon(container) {
    var geo = $(".geo", container).attr('title').split(',');
    var latlng = L.latLng(geo);
    console.log(latlng);
    return latlng
}*/
var map_data = "//" + location.host + location.pathname
console.log(map_data);
$.getJSON(map_data, function(data) {
    
    // SKOBBLER
    var skobblerApiKey = "3c996ca814d3ba1d95f98d4a8cdca880",
        skobblerUrl = 'http://tiles{s}.api.skobbler.net/tiles/{z}/{x}/{y}.png?api_key=' + skobblerApiKey,
        skobblerAttribution =  'Map data &copy; <a href="http://www.openstreetmap.org" target="_blank">OpenStreetMap</a> contributors, <a href="http://www.openstreetmap.org/copyright" target="_blank">Terms</a>, Tiles courtesy of <a href="http://www.skobbler.com" target="_blank">skobbler</a>';

    // OPENSTREETMAP
    var osmUrl = 'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
        osmAttribution = '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors';


    var skobblerMap = L.tileLayer(skobblerUrl, { subdomains: [1,2,3,4], attribution: skobblerAttribution, maxZoom: 18 }),
        osmMap =      L.tileLayer(osmUrl, { attribution: osmAttribution });
        
    var panopins = [];
    var allMarkers = [];
    
    $.each(data, function( index, value ) {
        var position = L.latLng(value[0]);
        panopin = L.marker(position).bindPopup("<b> PANO </b>").openPopup();
        panopins.push(panopin);
        allMarkers.push(position);
    });   

    var bounds = L.latLngBounds(allMarkers);
    var cities = L.layerGroup(panopins);

    var map = L.map('map', {layers:[osmMap,cities]})

    map.fitBounds(bounds);

    var baseMaps = {
        "OpenStreetMap": osmMap,
        "Skobbler": skobblerMap
    };

    var overlayMaps = {
        "Panoramms":cities
    };
    L.control.layers(baseMaps, overlayMaps).addTo(map);

});



