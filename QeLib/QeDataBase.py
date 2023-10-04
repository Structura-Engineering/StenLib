import os
import sqlite3
from typing import Any, Optional

from QeLib.QeHelper import QeHelper

TABLE1 = {
    "ID1": ["VALUE1", "VALUE2", "VALUE3"],
    "ID2": ["VALUE1", "VALUE2", "VALUE3"],
    "ID3": ["VALUE1", "VALUE2", "VALUE3"],
}


class QeDataBase(QeHelper):
    """A helper class for working with SQLite databases.

    Methods:
        connect_to_database(file: Optional[str] = None) -> sqlite3.Connection:
            Connect to the database.
        insert_data(
            data: dict, table: str, file: Optional[str] = None) -> None:
            Insert data into the database.
        delete_data(
            data: dict, table: str, file: Optional[str] = None) -> None:
            Delete data from the database.
        retrieve_data(
            data: dict, table: str, file: Optional[str] = None) -> dict:
            Retrieve data from the database.
    """

    @classmethod
    def connect_to_database(cls, file: str) -> sqlite3.Connection:
        """Connect to the database.

        Args:
            file (str): The name of the database file.
                Default is DEFAULT_DB_FILE.

        Returns:
            sqlite3.Connection: A connection to the database.
        """
        return sqlite3.connect(
            os.path.join(cls.data_path_generator(), f"{file}.sqlite")
        )

    @classmethod
    def insert_data(cls, data: dict[Any, Any], file: str) -> None:
        """Insert data into the database.

        Args:
            data (dict): The data to be inserted where keys are table names and values are lists of values.
            table (str): The name of the table to insert the data into.
            file (str): The name of the database file.
                Default is DEFAULT_DB_FILE.
        """
        with cls.connect_to_database(file) as conn:
            conn.execute(
                f"CREATE TABLE IF NOT EXISTS {dict_name} (id TEXT, value STRING)"
            )

    @classmethod
    def delete_data(cls, table: str, file: str) -> None:
        """Delete data from the database.

        Args:
            data (dict): The data to be deleted.
            table (str): The name of the table to delete the data from.
            file (str): The name of the database file.
                Default is DEFAULT_DB_FILE.
        """

    @classmethod
    def retrieve_data(cls, table: str, file: str) -> dict:
        """Retrieve data from the database.

        Args:
            table (str): The name of the table to retrieve the data from.
            file (str): The name of the database file.
                Default is DEFAULT_DB_FILE.

        Returns:
            dict: The retrieved data where keys are IDs and values are lists of values.
        """
        result = {}
        with cls.connect_to_database(file) as conn:
            cursor = conn.execute(f"SELECT * FROM {table}")
            for row in cursor.fetchall():
                id, value = row
                if id not in result:
                    result[id] = []
                result[id].append(cls.destringification(value))

        return result


QeDataBase.insert_data(data=TABLE1)
