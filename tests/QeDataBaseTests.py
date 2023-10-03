import unittest

from QeLib.QeDataBase import QeDataBase


class TestQeDataBase(unittest.TestCase):
    def test_create_table(self):
        # Test creating a table
        QeDataBase.create_table("test_table")

        # Test that the table was created
        with QeDataBase._connect_to_database() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name='test_table'"
            )
            result = cursor.fetchone()
            self.assertEqual(result[0], "test_table")

    def test_delete_table(self):
        # Test deleting a table
        QeDataBase.delete_table("test_table")

        # Test that the table was deleted
        with QeDataBase._connect_to_database() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name='test_table'"
            )
            result = cursor.fetchone()
            self.assertIsNone(result)


TestQeDataBase().test_create_table()
# TestQeDataBase().test_delete_table()
