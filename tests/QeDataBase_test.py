import sqlite3
import unittest

from QeLib.QeDataBase import QeDataBase


class TestQeDataBase(unittest.TestCase):
    def setUp(self):
        self.db_file_name = "test_database"
        self.table_name = "test_table"
        self.data = {
            "COL1": ["VALUE1", "VALUE2", "VALUE3"],
            "COL2": ["VALUE1", "VALUE2", "VALUE3"],
            "COL3": ["VALUE1", "VALUE2", "VALUE3"],
        }

    def test_connect_to_database(self):
        conn = QeDataBase.connect_to_database(self.db_file_name)
        self.assertIsInstance(conn, sqlite3.Connection)

    def test_insert_data(self):
        QeDataBase.insert_data(self.data, self.table_name, self.db_file_name)
        conn = QeDataBase.connect_to_database(self.db_file_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {self.table_name}")
        result = cursor.fetchone()
        self.assertEqual(result, self.data["COL1"])
        self.assertEqual(result, self.data["COL2"])
        self.assertEqual(result, self.data["COL3"])

    def test_delete_data(self):
        QeDataBase.insert_data(self.data, self.table_name, self.db_file_name)
        QeDataBase.delete_data(self.data, self.table_name, self.db_file_name)
        conn = QeDataBase.connect_to_database(self.db_file_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {self.table_name}")
        result = cursor.fetchone()
        self.assertIsNone(result)


TestQeDataBase()
