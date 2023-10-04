import sqlite3
from typing import Any, Optional

class QeDataBase:
    @classmethod
    def connect_to_database(cls, file: str) -> sqlite3.Connection: ...
    @classmethod
    def insert_data(
        cls, data: dict[Any, Any], table: str, file: Optional[str] = None
    ) -> None: ...
    @classmethod
    def delete_data(
        cls,
        data: Optional[dict] = None,
        table: Optional[str] = None,
        file: Optional[str] = None,
    ) -> None: ...
    @classmethod
    def retrieve_data(
        cls, data: dict, table: str, file: Optional[str] = None
    ) -> dict: ...
