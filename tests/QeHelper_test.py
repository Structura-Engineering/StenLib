import json
import os
import unittest

from QeLib.QeHelper import QeHelper


class TestQeHelper(unittest.TestCase):
    def test_alphanumeric_id_generator(self):
        assert isinstance(QeHelper.alphanumeric_id_generator(), str)
        assert len(QeHelper.alphanumeric_id_generator()) == 6
        assert len(QeHelper.alphanumeric_id_generator(10)) == 10
        assert len(QeHelper.alphanumeric_id_generator(-10)) == 10

    def test_data_path_generator(self):
        assert isinstance(QeHelper.data_path_generator(), str)
        assert os.path.exists(QeHelper.data_path_generator())

    def test_stringification(self):
        assert isinstance(QeHelper.stringification({}), str)
        assert json.loads(QeHelper.stringification({})) == {}

    def test_destringification(self):
        assert isinstance(QeHelper.destringification("{}"), dict)
        assert QeHelper.destringification('{"key": "value"}') == {"key": "value"}
