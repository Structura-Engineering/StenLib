import random
import string


def complex_id_generator(char_len=6):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(char_len))
