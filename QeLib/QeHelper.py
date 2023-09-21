import random
import string

from PySide6.QtCore import QPoint
from PySide6.QtWidgets import QApplication


def complex_id_generator(char_len=6):
    """see *.pyi file for docstring"""
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(abs(char_len)))


def center_ui_on_screen(ui) -> None:
    """see *.pyi file for docstring"""
    screen_center = QApplication.primaryScreen().geometry().center()
    ui_size = ui.size()
    ui.move(screen_center - QPoint(ui_size.width() // 2, ui_size.height() // 2))


def set_ui_size(ui, size=None) -> None:
    """see *.pyi file for docstring"""
    if size is None:
        size = ui.minimumSizeHint()
    ui.resize(*size)


def toggle_ui_visibility(uis) -> None:
    """Toggles the visibility of UI(s)."""
    for ui in uis:
        ui.setVisible(not ui.isVisible())
        if ui.isVisible():
            center_ui_on_screen(ui)


def switch_modules(module) -> None:
    """Switches the modules."""
    current_index = module.currentIndex()
    new_index = (current_index + 1) % module.count()
    module.setCurrentIndex(new_index)


def fit_scene_in_view(instance) -> None:
    """Fits the scene in the view."""
    instance.fitInView(instance.sceneRect(), AspectRatioModeTypes.KeepAspectRatio.value)
