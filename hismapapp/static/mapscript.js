var full_url = window.location.pathname;
console.log(full_url);
var url_array = full_url.split('/')
console.log(url_array)
const url_source = '/hismapapp/geojson/' + url_array[3]
console.log(url_source)

var osm = new ol.layer.Tile({
    source: new ol.source.OSM(),
    title: 'OpenStreetMap',
    baseLayer: true,
});

var stamen = new ol.layer.Tile({
    source: new ol.source.Stamen({ layer: 'toner' }),
    title: 'Stamen Toner',
    baseLayer: true,
    visible: false
});

var style = function(feature, resolution){
    var color = 'red';
    return new ol.style.Style({
        image: new ol.style.Circle({
            fill: new ol.style.Fill({ color: color}),
            stroke: new ol.style.Stroke ({color: 'white', width:1 }),
            radius: 5
        })
    })
};


var source = new ol.source.Vector({
    format: new ol.format.GeoJSON(),
    url: url_source
})

var historical_event = new ol.layer.Vector({
    source: source,
    title:'Historical Event',
    style: style,
    name: 'historical_event',
});

var view = new ol.View({
    center: ol.proj.fromLonLat([10.88, 50.89]),
    zoom: 6
})

var map = new ol.Map({
    target: 'map',
    layers: [osm, stamen, historical_event],
    view: view
});

var legend = new ol.control.LayerSwitcher();
map.addControl ( legend );

console.log(historical_event)
