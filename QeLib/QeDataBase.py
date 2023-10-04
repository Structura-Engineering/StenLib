import os
import sqlite3
from typing import Optional

from QeLib.QeHelper import QeHelper

data = {
    "COL1": ["VALUE1", "VALUE2", "VALUE3"],
    "COL2": ["VALUE1", "VALUE2", "VALUE3"],
    "COL3": ["VALUE1", "VALUE2", "VALUE3"],
}


class QeDataBase(QeHelper):
    """A helper class for working with SQLite databases.

    Attributes:
        DEFAULT_DB_file (str): The default name for the database file.

    Methods:
        connect_to_database(file: Optional[str] = None) -> sqlite3.Connection:
            Connect to the database.
        insert_data(
            data: dict, table: str, file: Optional[str] = None) -> None:
            Insert data into the database.
        delete_data(
            data: dict, table: str, file: Optional[str] = None) -> None:
            Delete data from the database.
    """

    DEFAULT_DB_FILE = "database"

    @classmethod
    def connect_to_database(cls, file: Optional[str] = None) -> sqlite3.Connection:
        """Connect to the database.

        Args:
            file (str): The name of the database file.
                Default is DEFAULT_DB_FILE.

        Returns:
            sqlite3.Connection: A connection to the database.
        """
        if file is None:
            file = cls.DEFAULT_DB_FILE

        return sqlite3.connect(
            os.path.join(cls.data_path_generator(), f"{file}.sqlite")
        )

    @classmethod
    def insert_data(cls, data: dict, table: str, file: Optional[str] = None) -> None:
        """Insert data into the database.

        Args:
            data (dict): The data to be inserted.
            table (str): The name of the table to insert the data into.
            file (str): The name of the database file.
                Default is DEFAULT_DB_file.
        """
        with cls.connect_to_database(file) as conn:
            conn.execute(f"CREATE TABLE IF NOT EXISTS {table} (id INTEGER PRIMARY KEY)")
            # TODO: insert data using stringification

    @classmethod
    def delete_data(cls, data: dict, table: str, file: Optional[str] = None) -> None:
        """delete data from the database.

        Args:
            data (dict): The data to be deleted.
            table (str): The name of the table to delete the data from.
            file (str): The name of the database file.
                Default is DEFAULT_DB_file.
        """
        # NOTE: if data is not None, delete data.
        # NOTE: if data is None, delete table.
        # NOTE: if data is None and table is None, delete file.

    @classmethod
    def retrieve_data(cls, data: dict, table: str, file: Optional[str] = None) -> dict:
        """Retrieve data from the database.

        Args:
            data (dict): The data to be retrieved.
            table (str): The name of the table to retrieve the data from.
            file (str): The name of the database file.
                Default is DEFAULT_DB_file.
        """
        # TODO: retrieve data using destringification
