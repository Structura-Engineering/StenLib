import os
import unittest

from QeLib.QeDataBase import QeDataBase

# TODO fix tests not importing classes correctly.


class TestQeDataBase(unittest.TestCase):
    def setUp(self):
        self.test_file_name = "test_file"
        self.test_data = {"test_key": [[1, 2], [3, 4]]}

    def tearDown(self):
        if os.path.exists(str(QeDataBase.load(self.test_file_name))):
            os.remove(str(QeDataBase.load(self.test_file_name)))

    def test_write_and_read(self):
        QeDataBase.write(self.test_data, self.test_file_name)
        read_data = QeDataBase.read(self.test_file_name)
        self.assertEqual(self.test_data, read_data)

    def test_create_and_delete(self):
        QeDataBase.create(self.test_file_name)
        self.assertTrue(os.path.exists(str(QeDataBase.load(self.test_file_name))))
        QeDataBase.delete(self.test_file_name)
        self.assertFalse(os.path.exists(str(QeDataBase.load(self.test_file_name))))
