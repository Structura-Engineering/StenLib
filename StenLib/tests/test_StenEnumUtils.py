import unittest

from StenLib.StenEnumUtils import EnumUtils


class TestEnumUtils(unittest.TestCase):
    """Test case for EnumUtils class."""

    def test_get_all_values(self):
        """
        Test the get_all_values method of EnumUtils.

        Returns:
            None
        """

        class ExampleEnum(EnumUtils):
            A = 1
            B = 2
            C = 3

        result = ExampleEnum.get_all_values()
        expected_result = [ExampleEnum.A, ExampleEnum.B, ExampleEnum.C]
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
