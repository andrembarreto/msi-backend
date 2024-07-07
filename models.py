from peewee import Model, CharField, ForeignKeyField, DateTimeField, AutoField, FloatField, fn, Field

from database import db
from shapely import wkb


class BaseModel(Model):
    class Meta:
        database = db


class BusLine(BaseModel):
    id = CharField(primary_key=True)


class Journey(BaseModel):
    id = AutoField()
    bus_line = ForeignKeyField(BusLine, backref='journeys')


class GeometryField(Field):
    field_type = 'geometry'

    def db_value(self, value):
        return fn.ST_GeomFromText(*value)

    def python_value(self, value):
        return wkb.loads(value)


class JourneyPoint(BaseModel):
    id = AutoField()
    journey = ForeignKeyField(Journey, backref='journey_points')
    geometry = GeometryField()
    timestamp = DateTimeField()
    acceleration_x = FloatField()
    acceleration_y = FloatField()
    acceleration_z = FloatField()
    rotation_x = FloatField()
    rotation_y = FloatField()
    rotation_z = FloatField()
