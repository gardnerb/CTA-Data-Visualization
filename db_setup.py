import peewee
from peewee import *

ctadb = MySQLDatabase('cta', user='ctauser')

class baseTable(peewee.Model):
	class Meta:
		database = ctadb

class busStop(baseTable):
	stop_id = peewee.IntegerField()
	street = peewee.CharField()
	cross_street = peewee.CharField()
	boardings = peewee.FloatField()
	alightings = peewee.FloatField()
	daytype = peewee.CharField()
	loc_x = peewee.DecimalField(max_digits="12", decimal_places=8)
	loc_y = peewee.DecimalField(max_digits="12", decimal_places=8)

class Route(baseTable):
	route_num = peewee.CharField()
	stop = peewee.ForeignKeyField(busStop, related_name='routes')


if __name__ == "__main__":
	busStop.create_table()
	Route.create_table()
