import json
from typing import Any
import psycopg

from db_connection import DBConnection


class PostgreSqlDBconnection(DBConnection):
    def __init__(self) -> None:
        self.__info = self.__load_db_info()
        self.__connection = None

    def connect(self) -> None:
        if self.__connection is None:
            self.__connection = psycopg.connect(**self.__info)

    def disconnect(self) -> None:
        if self.__connection is not None:
            self.__connection.close()
            self.__connection = None

    def commit(self) -> None:
        if self.__connection is not None:
            self.__connection.commit()

    def fetch_one(self, query: str, params: tuple[Any, ...]) -> dict[str, Any]:
        if self.__connection is not None:
            with self.__connection.cursor() as cursor:
                cursor.execute(query, params)
                result = cursor.fetchone()

            return result
        else:
            return None

    def execute_query(self, query: str, params: tuple[Any, ...]) -> None:
        if self.__connection is not None:
            with self.__connection.cursor() as cursor:
                cursor.execute(query, params)

    def __load_db_info(self) -> dict[str, Any]:
        with open('.db_info.json', 'r') as info_file:
            return json.load(info_file)
