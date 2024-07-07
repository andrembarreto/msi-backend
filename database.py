from peewee import PostgresqlDatabase
import json

with open('.db_info.json', 'r') as db_info_file:
    db_info = json.load(db_info_file)

db = PostgresqlDatabase('urban_mobility', **db_info)

def initialize_database():
    db.connect()
    from models import BusLine, Journey, JourneyPoint
    db.create_tables([BusLine, Journey, JourneyPoint], safe=True)

def close_database():
    if not db.is_closed():
        db.close()
