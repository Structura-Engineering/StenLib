import unittest
from StenLib.StenUtils import Utils


class TestUtils(unittest.TestCase):
    """Test case for Utils class."""

    def test_rstr(self):
        """
        Test the rstr method of Utils.

        Returns:
            None
        """
        result = Utils.rstr("Hello, World!")
        self.assertEqual(result, "!dlroW ,olleH")

    def test_alphanumeric_id_generator(self):
        """
        Test the alphanumeric_id_generator method of Utils.

        Returns:
            None
        """
        result = Utils.alphanumeric_id_generator()
        self.assertEqual(len(result), 6)
        self.assertTrue(result.isalnum())

        result_10_chars = Utils.alphanumeric_id_generator(10)
        self.assertEqual(len(result_10_chars), 10)
        self.assertTrue(result_10_chars.isalnum())

        result_negative_chars = Utils.alphanumeric_id_generator(-10)
        self.assertEqual(len(result_negative_chars), 10)
        self.assertTrue(result_negative_chars.isalnum())

        original_result = Utils.alphanumeric_id_generator(reversed=False)
        result_reversed = original_result[::-1]
        self.assertEqual(result_reversed, original_result[::-1])
        self.assertTrue(result_reversed.isalnum())

    def test_alphanumeric_id_generator_secrets(self):
        """
        Test the alphanumeric_id_generator method of Utils with secrets module.

        Returns:
            None
        """
        result = Utils.alphanumeric_id_generator(use_secrets=True)
        self.assertEqual(len(result), 6)
        self.assertTrue(result.isalnum())

        result_10_chars = Utils.alphanumeric_id_generator(10, use_secrets=True)
        self.assertEqual(len(result_10_chars), 10)
        self.assertTrue(result_10_chars.isalnum())

        result_negative_chars = Utils.alphanumeric_id_generator(-10, use_secrets=True)
        self.assertEqual(len(result_negative_chars), 10)
        self.assertTrue(result_negative_chars.isalnum())

        original_result = Utils.alphanumeric_id_generator(
            reversed=True, use_secrets=True
        )
        result_reversed = original_result[::-1]
        self.assertEqual(result_reversed, original_result[::-1])
        self.assertTrue(result_reversed.isalnum())


if __name__ == "__main__":
    unittest.main()
