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

    var map = new ol.Map({
        target: 'map',
        layers: [osm, stamen,],
        view: new ol.View({
            center: ol.proj.fromLonLat([22.8, 51.35]),
            zoom: 8
        })
    });



    var legend = new ol.control.LayerSwitcher();
    map.addControl ( legend );