import random
import string

from PySide6.QtCore import QPoint
from PySide6.QtWidgets import QApplication


def complex_id_generator(char_len=6):
    """see *.pyi file for docstring"""
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(abs(char_len)))


def center_ui_on_screen(ui):
    """see *.pyi file for docstring"""
    screen_center = QApplication.primaryScreen().geometry().center()
    ui_size = ui.size()
    ui.move(screen_center - QPoint(ui_size.width() // 2, ui_size.height() // 2))
