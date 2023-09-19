import secrets
import string


def complex_id_generator(char_len: int = 6) -> str:
    """Generate a complex ID."""
    chars = string.ascii_letters + string.digits
    return "".join(secrets.choice(chars) for _ in range(char_len))
