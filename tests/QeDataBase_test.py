import os
import unittest

from QeLib.QeDataBase import QeDataBase


class TestQeDataBase(unittest.TestCase):
    def setUp(self):
        self.file_path = "test.json"
        self.data = {
            "list1": [[1, 2, 3], [4, 5, 6]],
            "list2": [[7, 8, 9], [10, 11, 12]],
        }

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_write_and_read(self):
        QeDataBase.write(self.data, self.file_path)
        result = QeDataBase.read(self.file_path)
        self.assertEqual(result, self.data)

    def test_create_and_delete(self):
        QeDataBase.create(self.file_path)
        self.assertTrue(os.path.exists(self.file_path))
        QeDataBase.delete(self.file_path)
        self.assertFalse(os.path.exists(self.file_path))


if __name__ == "__main__":
    unittest.main()
