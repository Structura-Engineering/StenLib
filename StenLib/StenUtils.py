import random
import secrets
import string


class Utils:
    """A collection of utility functions."""

    CHARS: str = string.ascii_letters + string.digits

    @staticmethod
    def rstr(s: str) -> str:
        """Reverse a given string.

        Args:
            s (str): The string to be reversed.

        Returns:
            str: The reversed string.

        Example:
            >>> Utils.rstr('Hello, World!')
            "!dlroW ,olleH"
        """
        return s[::-1]

    @classmethod
    def alphanumeric_id_generator(
        cls,
        char_len: int = 6,
        use_secrets: bool = False,
        reversed: bool = False,
    ) -> str:
        """Generate a random alphanumeric ID.

        Args:
            char_len (int, optional):
                Absolute length of the generated ID. Defaults to 6.
            use_secrets (bool, optional):
                If True, use the secrets module for more secure random choices.
                    Defaults to False.
            reversed (bool, optional):
                If True, reverse the generated ID using the rstr method.
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
        randomizer = secrets if use_secrets else random
        generated_id = ''.join(
            randomizer.choice(cls.CHARS) for _ in range(abs(char_len))
        )
        return cls.rstr(generated_id) if reversed else generated_id
