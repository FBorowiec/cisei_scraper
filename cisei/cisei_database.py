import psycopg2
from psycopg2.extras import Json


class Database:
    HOST: str = "172.18.0.2"
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
            with self.db_connection:
                self.cursor.execute(query)
                return self.cursor.fetchone()

    def query_fetch_all(self, path: str, **kwargs) -> list:
        with open(path, "r", encoding="utf-8") as query_file:
            query: str = query_file.read()
            with self.db_connection:
                self.cursor.execute(query, kwargs)
                return self.cursor.fetchall()

    def create_person_info_table(self) -> None:
        self.query_post("database/queries/create_person_info_table.sql")

    def add_person_info(self, person_info) -> None:
        self.query_post(
            "database/queries/add_person_info.sql",
            person_info.idx,
            person_info.surname,
            person_info.full_name,
            person_info.age,
            person_info.trip_date,
            person_info.registration_place,
            person_info.url,
            Json(person_info.details),
        )

    def display_person_info(self) -> None:
        self.query_fetch_all("database/queries/display_person_info.sql")

    def __del__(self) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
