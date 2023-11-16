import unittest

from hypothesis import given
from hypothesis import strategies as st

from StenLib.StenUtils import Utils


class TestUtils(unittest.TestCase):
    """A collection of utility functions."""

    @given(st.integers(), st.integers())
    def test_alphanumeric_id_generator(self, a, b):
        """Generate a random alphanumeric ID.

        Args:
            char_len (int, optional):
                Absolute length of the generated ID. Defaults to 6.
            use_secrets (bool, optional):
                If True, use the secrets module for more secure random choices.
                    Defaults to False.

        Returns:
            str: A randomly generated ID consisting of alphanumeric characters.

        Example:
            >>> alphanumeric_id_generator()
            "r9g3Yx"
            >>> alphanumeric_id_generator(10)
            "1z7y6W1h5Z"
            >>> alphanumeric_id_generator(-10)
            "2y6fRk5n8T"
        """
        your_instance = Utils()
        result = your_instance.alphanumeric_id_generator(a, b)
        self.assertIsNotNone(result)
