import os
import sqlite3

from QeLib.QeHelper import QeHelper


class QeDataBase(QeHelper):
    @classmethod
    def _connect_to_database(cls, file_name: str) -> sqlite3.Connection:
        """Connect to the database.

        Args:
            file_name (str): The name of the database file.

        Returns:
            sqlite3.Connection: A connection to the database.
        """
        return sqlite3.connect(
            os.path.join(cls.data_path_generator(), f"{file_name}.db")
        )
