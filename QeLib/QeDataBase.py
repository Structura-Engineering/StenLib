import os
import sqlite3
from typing import Optional

from QeLib.QeHelper import QeHelper


class QeDataBase(QeHelper):
    """A helper class for working with SQLite databases.

    Attributes:
        DEFAULT_DB_FILE_NAME (str): The default name for the database file.

    Methods:
        _connect_to_database(file_name: Optional[str] = None) -> sqlite3.Connection:
            Connect to the database.
        create_table(table_name: str, file_name: Optional[str] = None) -> None:
            Create a table in the database.
        delete_table(table_name: str, file_name: Optional[str] = None) -> None:
            Delete a table in the database.
    """

    DEFAULT_DB_FILE_NAME = "database"

    @classmethod
    def _connect_to_database(
        cls, file_name: Optional[str] = None
    ) -> sqlite3.Connection:
        """Connect to the database.

        Args:
            file_name (str): The name of the database file. Default is DEFAULT_DB_FILE_NAME.

        Returns:
            sqlite3.Connection: A connection to the database.
        """
        if file_name is None:
            file_name = cls.DEFAULT_DB_FILE_NAME

        return sqlite3.connect(
            os.path.join(cls.data_path_generator(), f"{file_name}.sqlite")
        )

    @classmethod
    def create_table(cls, table_name: str, file_name: Optional[str] = None) -> None:
        """Create a table in the database.

        Args:
            file_name (str): The name of the database file. Default is DEFAULT_DB_FILE_NAME.
            table_name (str): The name of the table to be created.
        """
        with cls._connect_to_database(file_name) as conn:
            conn.execute(
                f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY)"
            )

    @classmethod
    def delete_table(cls, table_name: str, file_name: Optional[str] = None) -> None:
        """Delete a table in the database.

        Args:
            file_name (str): The name of the database file. Default is DEFAULT_DB_FILE_NAME.
            table_name (str): The name of the table to be deleted.
        """
        with cls._connect_to_database(file_name) as conn:
            conn.execute(f"DROP TABLE IF EXISTS {table_name}")

    @classmethod
    def insert_data(cls, data: dict, table_name: str, file_name: Optional[str] = None):
        """Insert data into the database.

        Args:
            data (dict): The data to be inserted.
            table_name (str): The name of the table to insert the data into.
            file_name (str): The name of the database file. Default is DEFAULT_DB_FILE_NAME.
        """
        # TODO: Implement insert_data

    @classmethod
    def delete_data(cls, data: dict, table_name: str, file_name: Optional[str] = None):
        """delete data from the database.

        Args:
            data (dict): The data to be deleted.
            table_name (str): The name of the table to delete the data from.
            file_name (str): The name of the database file. Default is DEFAULT_DB_FILE_NAME.
        """
        # TODO: Implement delete_data
