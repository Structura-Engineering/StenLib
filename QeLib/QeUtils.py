import os
import random
import secrets
import string


class QeUtils:
    """A collection of utility functions."""

    CHARS: str = string.ascii_letters + string.digits

    @classmethod
    def alphanumeric_id_generator(
        cls, char_len: int = 6, use_secrets: bool = False
    ) -> str:
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
            'r9g3Yx'
            >>> alphanumeric_id_generator(10)
            '1z7y6W1h5Z'
            >>> alphanumeric_id_generator(-10)
            '2y6fRk5n8T'
        """
        randomizer = secrets if use_secrets else random
        return "".join(randomizer.choice(cls.CHARS) for _ in range(abs(char_len)))

    @staticmethod
    def data_path_generator() -> str:
        """Create the data path.

        Returns:
            str: The path to the data directory.
        """
        data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
        os.makedirs(data_path, exist_ok=True)
        return data_path
