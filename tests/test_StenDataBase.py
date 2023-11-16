import unittest

from hypothesis import given
from hypothesis import strategies as st

from StenLib.StenDataBase import DataBase


class TestDataBase(unittest.TestCase):
    """A class for managing JSON files."""

    @given(st.integers(), st.integers())
    def test___init__(self, a, b):
        """Initialize the DataBase class.

        Args:
            file_name (str): The name of the JSON file.
            data_folder (str, optional): The name of the data folder. Defaults to "data".
        """
        your_instance = DataBase()
        result = your_instance.__init__(a, b)
        self.assertIsNotNone(result)

    @given(st.integers(), st.integers())
    def test_get(self, a, b):
        """Get the value for a key.

        Args:
            key (str): The key to get the value for.
        """
        your_instance = DataBase()
        result = your_instance.get(a, b)
        self.assertIsNotNone(result)

    @given(st.integers(), st.integers())
    def test_set(self, a, b):
        """Set the value for a key.

        Args:
            key (str): The key to set the value for.
            value (Any): The value to set.
        """
        your_instance = DataBase()
        result = your_instance.set(a, b)
        self.assertIsNotNone(result)

    @given(st.integers(), st.integers())
    def test_delete(self, a, b):
        """Delete a key.

        Args:
            key (str): The key to delete.
        """
        your_instance = DataBase()
        result = your_instance.delete(a, b)
        self.assertIsNotNone(result)

    @given(st.integers(), st.integers())
    def test_save(self, a, b):
        """Save the data to the file."""
        your_instance = DataBase()
        result = your_instance.save(a, b)
        self.assertIsNotNone(result)

    @given(st.integers(), st.integers())
    def test_data_path_generator(self, a, b):
        """Create the data path.

        Args:
            data_folder (str, optional):
                The name of the data folder. Defaults to "data".

        Returns:
            str: The path to the data directory.
        """
        your_instance = DataBase()
        result = your_instance.data_path_generator(a, b)
        self.assertIsNotNone(result)
