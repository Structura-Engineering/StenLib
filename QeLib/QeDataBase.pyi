import sqlite3
from typing import Optional

class QeDataBase:
    @classmethod
    def _connect_to_database(
        cls, file_name: Optional[str] = None
    ) -> sqlite3.Connection: ...
    @classmethod
    def create_table(cls, table_name: str, file_name: Optional[str] = None) -> None: ...
    @classmethod
    def delete_table(cls, table_name: str, file_name: Optional[str] = None) -> None: ...
