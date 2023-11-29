import psycopg2
from datetime import datetime
import json

class MobilityDataBaseController:
    def __init__(self):
        db_info = self.get_db_info()
        self.connection = psycopg2.connect(database=db_info['database'],
                                            user=db_info['user'],
                                            host=db_info['host'],
                                            password=db_info['password'],
                                            port=db_info['port'])
        
        self.cursor = self.connection.cursor()
    
    def store_journey_entries(self, mobility_data: list[dict]) -> bool:
        self.register_journey_bus_line(mobility_data[0]['bus_line'])

        journey_id = self.fetch_journey_id()

        for journey_point in mobility_data[1:]:
            journey_point['timestamp'] = datetime.strptime(journey_point['timestamp'], "%a %b %d %H:%M:%S %Y %Z")
            journey_point['journey_id'] = journey_id

            self.cursor.execute('''INSERT INTO mobility.ponto_jornada(
                                        aceleracao_x, aceleracao_y, aceleracao_z,
                                        rotacao_x, rotacao_y, rotacao_z, orientacao,
                                        id_jornada, timestamp, latitude, longitude)
                                    VALUES
                                        (%(acceleration_x)s,%(acceleration_y)s,%(acceleration_z)s,
                                        %(rotation_x)s,%(rotation_y)s,%(rotation_z)s,
                                        \'%(device_orientation)s\',%(journey_id)s,%(timestamp)s,
                                        %(latitude)s,%(longitude)s)''', journey_point)
        self.connection.commit()
        self.connection.close()

    def register_journey_bus_line(self, line_id: str):
        self.cursor.execute('SELECT * FROM mobility.linha_onibus l WHERE l.id_linha = %(line_id)s', {"line_id": line_id}) # checking if line is already registered
        
        if len(self.cursor.fetchall()) == 0:
            self.cursor.execute('INSERT INTO mobility.linha_onibus(id_linha) VALUES(%(line_id)s)', {"line_id": line_id})

        self.cursor.execute('INSERT INTO mobility.jornada(id_linha) VALUES(%(line_id)s)', {"line_id": line_id})
        
        self.connection.commit()

    def fetch_journey_id(self):
        self.cursor.execute('SELECT max(id_jornada) FROM mobility.jornada')
        result = self.cursor.fetchall()
        self.connection.commit()

        if result is None:
            raise Exception("Journey Id not Found")
        
        return result[0][0]
    
    def get_db_info(self) -> dict:
        with open('db_info.json', "r") as db_info_file:
            db_info = json.loads(db_info_file.read())
        db_info_file.close()
        return db_info
