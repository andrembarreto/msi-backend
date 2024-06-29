from peewee import Model, CharField, ForeignKeyField, DateTimeField, AutoField, FloatField

from database import db


class BaseModel(Model):
    class Meta:
        database = db


class BusLine(BaseModel):
    id = CharField(primary_key=True)


class Journey(BaseModel):
    id = AutoField()
    bus_line = ForeignKeyField(BusLine, backref='journeys')


class JourneyPoint(BaseModel):
    # TODO: add custom 'coordinate' field to replace latitude and longitude
    id = AutoField()
    journey = ForeignKeyField(Journey, backref='journey_points')
    timestamp = DateTimeField()
    latitude = FloatField()
    longitude = FloatField()
    acceleration_x = FloatField()
    acceleration_y = FloatField()
    acceleration_z = FloatField()
    rotation_x = FloatField()
    rotation_y = FloatField()
    rotation_z = FloatField()
