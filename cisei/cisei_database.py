from typing import Optional, Tuple

import psycopg2
from psycopg2.extras import Json

from data_types.person_info import PersonInfo


class Database:
    HOST: str = "database_pg"
    PORT: str = "5432"
    DB_NAME: str = "database_pg"
    USER: str = "postgres"
    PASSWORD: str = "postgres"

    def __init__(self) -> None:
        self.conn = psycopg2.connect(
            host=self.HOST,
            database=self.DB_NAME,
            port=self.PORT,
            user=self.USER,
            password=self.PASSWORD,
        )
        self.cursor = self.conn.cursor()

        self.create_person_info_table()

    def query_post(self, path: str, **kwargs) -> None:
        with open(path, "r", encoding="utf-8") as query_file:
            query: str = query_file.read()
            with self.conn:
                self.cursor.execute(query, kwargs)
                self.conn.commit()

    def query_fetch_one(self, path: str) -> tuple:
        with open(path, "r", encoding="utf-8") as query_file:
            query: str = query_file.read()
            with self.conn:
                self.cursor.execute(query)
                return self.cursor.fetchone()

    def query_fetch_all(self, path: str, **kwargs) -> list:
        with open(path, "r", encoding="utf-8") as query_file:
            query: str = query_file.read()
            with self.conn:
                self.cursor.execute(query, kwargs)
                return self.cursor.fetchall()

    def create_person_info_table(self) -> None:
        self.query_post("database/queries/create_person_info_table.sql")

    def add_person_info(self, person_info: PersonInfo) -> None:
        self.query_post(
            path="database/queries/add_person_info.sql",
            idx=person_info.idx,
            surname=person_info.surname,
            full_name=person_info.full_name,
            age=person_info.age,
            trip_date=person_info.trip_date,
            registration_place=person_info.registration_place,
            url=person_info.url,
            details=Json(person_info.details),
        )

    def display_person_info(self) -> None:
        self.query_fetch_all("database/queries/display_person_info.sql")

    def get_last_person_info(self) -> Optional[PersonInfo]:
        result: Tuple = self.query_fetch_one(
            "database/queries/get_last_person_info.sql"
        )
        if result:
            return PersonInfo(
                idx=result[1],
                surname=result[2],
                full_name=result[3],
                age=result[4],
                trip_date=result[5],
                registration_place=result[6],
                url=result[7],
                details=result[8],
            )

    def __del__(self) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
