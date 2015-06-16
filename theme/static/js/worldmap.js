//var map_data = "//" + location.host  + "worldmap.json"
var map_data = [site_url, "worldmap.json"].join("/");
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
    
    $.each(data, function( label, details ) {
        if ( details.lat != null  || details.lng != null ){
            var position = L.latLng(details.lat, details.lng);
            var title = details.title;
            var icon_url = [site_url,'sizes', label, label + '-icon.jpg'].join("/");
            var url = [site_url,details.url].join("/");
            var label = ([
                "<strong>" + title+ "</strong><br />",
                "<a href=" + url + "><img src=" + icon_url + " /></a><br />",
                "<a href=" + url + ">open</a>"
                ]).join("\n");
            panopin = L.marker(position).bindPopup(label).openPopup();
            panopins.push(panopin);
            allMarkers.push(position);
        };
    });   

    var bounds = L.latLngBounds(allMarkers);
    var cities = L.layerGroup(panopins);

    var map = L.map('worldmap', {layers:[osmMap,cities]})

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



