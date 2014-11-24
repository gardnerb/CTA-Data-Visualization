from bottle import route, run, view, template, static_file
from db_setup import busStop

ROOT_PATH = '/Users/bgardner/Desktop/ctadata/CTA-Data-Visualization/static'

@route('/map')
@view('views/heatmapview')
def map():
	stops = ""
	longitudes = ""
	latitudes = ""
	boardings = ""

	for stop in busStop.select():
		stops += str(stop.stop_id) + ","
		longitudes += str(stop.loc_x) + ","
		latitudes += str(stop.loc_y) + ","
		boardings += str(stop.boardings) + ","

	return dict(stop_list=stops, longs=longitudes, lats=latitudes, boardings=boardings);

@route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root=ROOT_PATH)


run(host='localhost', port='8040', debug=True)