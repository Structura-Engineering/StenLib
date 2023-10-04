import os
import sqlite3
import unittest

from QeLib.QeDataBase import QeDataBase


class TestQeDataBase(unittest.TestCase):
    def setUp(self):
        self._db_file = "test"
        self._table_name = "test_table"
        self._data = {"name": "John", "age": 30, "city": "New York"}

    def tearDown(self):
        os.remove(self._db_file)

    def test_create_table(self):
        QeDataBase.create_table(self._table_name, self._db_file)
        with sqlite3.connect(self._db_file) as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self._table_name}'"
            )
            result = cursor.fetchone()
            self.assertIsNotNone(result)

    def test_insert_data(self):
        QeDataBase.create_table(self._table_name, self._db_file)
        QeDataBase.insert_data(self._data, self._table_name, self._db_file)
        with sqlite3.connect(self._db_file) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {self._table_name}")
            result = cursor.fetchone()
            self.assertIsNotNone(result)
            self.assertEqual(result[0], self._data["name"])
            self.assertEqual(result[1], self._data["age"])
            self.assertEqual(result[2], self._data["city"])

    def test_delete_data(self):
        QeDataBase.create_table(self._table_name, self._db_file)
        QeDataBase.insert_data(self._data, self._table_name, self._db_file)
        QeDataBase.delete_data({"name": "John"}, self._table_name, self._db_file)
        with sqlite3.connect(self._db_file) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {self._table_name}")
            result = cursor.fetchone()
            self.assertIsNone(result)

    def test_delete_table(self):
        QeDataBase.create_table(self._table_name, self._db_file)
        QeDataBase.delete_table(self._table_name, self._db_file)
        with sqlite3.connect(self._db_file) as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self._table_name}'"
            )
            result = cursor.fetchone()
            self.assertIsNone(result)


TestQeDataBase().test_create_table
# TestQeDataBase().test_insert_data
# TestQeDataBase().test_delete_data
# TestQeDataBase().test_delete_table
