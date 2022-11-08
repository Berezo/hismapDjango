//map background

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

//style of data

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


//source of data

var full_url = window.location.pathname;
var url_array = full_url.split('/')
const url_source = '/hismapapp/geojson/' + url_array[3]
var source = new ol.source.Vector({
    format: new ol.format.GeoJSON(),
    url: url_source
})

//vector

var historical_event = new ol.layer.Vector({
    source: source,
    title:'Historical Event',
    style: style,
    name: 'historical_event',
});

//data

var view = new ol.View({
    center: ol.proj.fromLonLat([10.88, 50.89]),
    zoom: 6
})

//map

var map = new ol.Map({
    target: 'map',
    layers: [osm, stamen, historical_event],
    view: view
});

var legend = new ol.control.LayerSwitcher();
map.addControl ( legend );

// Selecting a point on the map changes its colour on the map,
// and in the side panel of the event to which the point refers

var style_select = function(feature, resolution){
    return new ol.style.Style({
        image: new ol.style.Circle({
        fill: new ol.style.Fill({ color: 'green'}),
        stroke: new ol.style.Stroke ({color: 'white', width:1 }),
        radius: 5
        })
    })
};

var select = new ol.interaction.Select({
    style: style_select,
});

map.addInteraction(select);

var selectedFeatures = select.getFeatures();

var accord_class = null;
var card_class = null;
var accord_class_select = "accordion-button collapsed text-white bg-success";
var card_class_select = "accordion-body collapsed text-white bg-success";

var card = null;

function onClick(id, callback) {
    document.getElementById(id).addEventListener('click', callback);
}

selectedFeatures.on(['add', 'remove'], function () {
    var names = selectedFeatures.getArray().map(function (feature) {
    return feature.get("pk");
});

if (names.length > 0) {
    accord = document.getElementById("accord" + names[0]);
    card = document.getElementById("card" + names[0]);
    accord_class = accord.className;
    card_class = card.className;
    accord.className = accord_class_select;
    card.className = card_class_select;
} else {
    accord.className = accord_class;
    card.className = card_class;
    edit_button = navigation.removeChild(edit_button)
    }
});

var geom_list = []
var id_click_list = []