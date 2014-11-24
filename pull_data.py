# data form: {u'on_street': u'JACKSON', u'cross_street': u'AUSTIN', u'boardings': u'183.4',
# 	u'month': u'2012-10-01T00:00:00', u'location': {u'latitude': u'41.87632184', u'needs_recoding': False,
# 	u'longitude': u'-87.77410482'}, u'stop_id': u'1', u'routes': u'126', u'daytype': u'Weekday',
# 	u'alightings': u'150.0'}

import json, urllib
import peewee
from peewee import *
from decimal import *

from db_setup import busStop, Route

entrypoint = 'http://data.cityofchicago.org/resource/mq3i-nnqe.json?'
app_token = '$$app_token=gqo7Im3NCljZcUezk4lSXH2yr'
limit = '&$limit=1000'
offset = '&$offset='
order = '&$order=stop_id'

offset_count = 0
while(offset_count < 12):
	query = entrypoint + app_token + limit + offset + str(offset_count*1000) + order
	queryurl = urllib.urlopen(query)
	data = json.loads(queryurl.read())
	if data == None:
		break

	try:
		for entry in data:
			if entry["stop_id"] == None:
				continue

			stop_id = int(entry['stop_id'])
			street = entry['on_street']
			cross_street = entry['cross_street']
			boardings = float(entry['boardings'])
			alightings = float(entry['alightings'])
			daytype = entry['daytype']
			loc_x = Decimal(entry['location']['longitude'])
			loc_y = Decimal(entry['location']['latitude'])

			bus_stop = busStop(stop_id=stop_id, street=street, cross_street=cross_street,
						boardings=boardings, alightings=alightings, daytype=daytype,
						loc_x=loc_x, loc_y=loc_y)
			bus_stop.save()

			if "routes" not in entry:
				continue
				
			routes = entry["routes"]
			related_stop = busStop.get(stop_id=stop_id)
			if "," in routes:
				routes = routes.split(",")
				for route in routes:
					r = Route(route_num=route, stop=related_stop)
					r.save()
			else:
				r = Route(route_num=routes, stop=bus_stop)
				r.save()
	except KeyError:
		print entry
		continue
		
	offset_count += 1

print 'done!'