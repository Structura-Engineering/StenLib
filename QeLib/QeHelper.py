import random
import string
import sys

# TODO: figure out how we can show the docstrings from the .pyi file on the method info box like it does with the type hints.


def complex_id_generator(char_len=6):
    """__doc__ = complex_id_generator.__doc__"""
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(abs(char_len)))


def center_ui_on_screen(screen_center, ui_size):
    """__doc__ = complex_id_generator.__doc__"""
    (x, y), (width, height) = screen_center, ui_size
    ui_position = (x - width // 2, y - height // 2)
    sys.argv.extend(["--window-position", f"{ui_position[0]},{ui_position[1]}"])
