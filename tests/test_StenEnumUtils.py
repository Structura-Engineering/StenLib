import unittest

from hypothesis import given
from hypothesis import strategies as st

from StenLib.StenEnumUtils import EnumUtils


class TestEnumUtils(unittest.TestCase):
    """A class that contains core methods for Enum."""

    @given(st.integers(), st.integers())
    def test_get_all_values(self, a, b):
        """
        Get all values of an Enum class as a list.

        Args:
            enum_class (Type[Enum]): The Enum class.

        Returns:
            list[Union[Enum, Type]]: A list of enum values.
        """
        your_instance = EnumUtils()
        result = your_instance.get_all_values(a, b)
        self.assertIsNotNone(result)
