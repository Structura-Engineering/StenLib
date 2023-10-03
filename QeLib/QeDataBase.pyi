import sqlite3

class QeDataBase:
    @classmethod
    def _connect_to_database(cls, file_name: str) -> sqlite3.Connection: ...
