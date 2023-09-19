import random
import string


class Helper:
    """Helper class for common functions"""

    @staticmethod
    def complex_id_generator(char_len: int = 6) -> str:
        """Generate a complex ID."""
        chars = string.ascii_letters + string.digits
        return "".join(random.choice(chars) for _ in range(char_len))
