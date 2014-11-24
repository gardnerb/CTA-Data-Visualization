<!DOCTYPE html>
<html>
<head>
	<title>CTA Heat Map</title>
	<style type="text/css">
	html {
		height: 100%;
	}
	body {
		min-height: 100%;
	}
	</style>
	<script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
	<script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?key=AIzaSyB10ggMkdbGJ3qwi8sqbrsEcCq_IyvdaRc"></script>
	<script type="text/javascript" src="static/heatmap.min.js"></script>
	<script type="text/javascript" src="static/gmaps-heatmap.js"></script>
	<script>

	//get data passed to template
	function grabData() {
		var b_data = $("#boardings").html().split(",");
		var lat_data = $("#lats").html().split(",");
		var long_data = $("#longs").html().split(",");

		var data_arr = []
		for (var i=0; i < b_data.length - 1; i++) {
			var point = {
				lat: lat_data[i],
				lng: long_data[i],
				count: i,
			};
			data_arr.push(point);
		}
		console.log(data_arr);
		var dataForMap = {
			max: 100,
			data: data_arr,
		}
		return dataForMap;
	}

	function initialize() {
		var mapOptions = {
			center: new google.maps.LatLng(41.850033, -87.6500523),
			zoom: 10,
			minZoom: 9,
			maxZoom:12
		};
		var heatmapOpts = {
			"radius": 0.005,
			"maxOpacity": 1,
			"scaleRadius": true,
			"useLocalExtrema": true,
			latField: 'lat',
			lngField: 'lng',
			valueField: 'count',
		}

		var map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);
		heatmap = new HeatmapOverlay(map, heatmapOpts)
		
		dataForMap = grabData();
		heatmap.setData(dataForMap);
	}	


	google.maps.event.addDomListener(window, 'load', initialize);
	</script>
</head>
<body>
<div id="map-canvas" style="width: 100%; height:600px"></div>
<div id="data" style="display: none;">
	<div id="stop_list">{{stop_list}}</div>
	<div id="longs">{{longs}}</div>
	<div id="lats">{{lats}}</div>
	<div id="boardings">{{boardings}}</div>
</div>
</body>
</html>