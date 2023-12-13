import unittest

from StenLib.StenUtils import Utils


class TestUtils(unittest.TestCase):
    """Test case for Utils class."""

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


if __name__ == "__main__":
    unittest.main()
