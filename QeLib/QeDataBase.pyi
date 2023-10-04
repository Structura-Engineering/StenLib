import sqlite3
from typing import Optional

class QeDataBase:
    @classmethod
    def connect_to_database(cls, file: Optional[str] = None) -> sqlite3.Connection: ...
    @classmethod
    def insert_data(
        cls, data: dict, table: str, file: Optional[str] = None
    ) -> None: ...
    @classmethod
    def delete_data(
        cls, data: dict, table: str, file: Optional[str] = None
    ) -> None: ...
    @classmethod
    def retrieve_data(
        cls, data: dict, table: str, file: Optional[str] = None
    ) -> dict: ...
