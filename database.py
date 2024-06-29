from peewee import SqliteDatabase

db = SqliteDatabase('mobility.db')

def initialize_database():
    db.connect()
    from models import BusLine, Journey, JourneyPoint
    db.create_tables([BusLine, Journey, JourneyPoint], safe=True)

def close_database():
    if not db.is_closed():
        db.close()
