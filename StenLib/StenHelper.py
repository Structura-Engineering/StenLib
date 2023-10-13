from typing import List, Optional, Tuple

from PySide6.QtCore import QPoint, Qt
from PySide6.QtWidgets import (
    QApplication,
    QFormLayout,
    QGraphicsView,
    QGridLayout,
    QHBoxLayout,
    QLayout,
    QStackedLayout,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)


class StenHelper:
    """A collection of helper functions."""

    @staticmethod
    def center_ui_on_screen(ui: QWidget) -> None:
        """
        Centers a QWidget on the screen.

        Args:
            ui (QWidget): The QWidget to be centered on the screen.
        """
        ui.move(
            QApplication.primaryScreen().geometry().center()
            - QPoint(ui.size().width() // 2, ui.size().height() // 2)
        )

    @staticmethod
    def set_ui_size(ui: QWidget, size: Optional[Tuple[int, int]] = None) -> None:
        """
        Sets the size of a QWidget.

        Args:
            ui (QWidget): The QWidget whose size is to be set.
            size (tuple[int, int], optional): The width and height to set the QWidget.
                If None, it will be set to the default size hint.

        """
        ui.resize(*size) if size else ui.resize(ui.sizeHint())

    @classmethod
    def toggle_ui_visibility(cls, uis: List[QWidget]) -> None:
        """
        Toggles the visibility of a list of QWidgets.

        Args:
            uis (list[QWidget]): List of QWidgets whose visibility will be toggled.
        """
        for ui in uis:
            ui.setVisible(not ui.isVisible())
            if ui.isVisible():
                cls.center_ui_on_screen(ui)

    @staticmethod
    def switch_modules(module: QStackedWidget) -> None:
        """
        Switches the current module in a QStackedWidget.

        Args:
            module (QStackedWidget): The QStackedWidget containing the modules.
        """
        module.setCurrentIndex((module.currentIndex() + 1) % module.count())

    @staticmethod
    def fit_scene_in_view(instance: QGraphicsView) -> None:
        """
        Fits the scene inside a QGraphicsView while maintaining aspect ratio.

        Args:
            instance (QGraphicsView): The QGraphicsView containing the scene.
        """
        instance.fitInView(instance.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)

    @staticmethod
    def layout_handler(layout_type: str = "VBox") -> QLayout:
        """
        Initialize the LayoutHandler with a specified layout type.

        Args:
            layout_type (str): Type of layout.
                Options: 'VBox', 'HBox', 'Grid', 'Form', or 'Stacked'.
                Default is 'VBox'.

        Returns:
            QLayout: A layout object.
        """
        return {
            "VBox": QVBoxLayout,
            "HBox": QHBoxLayout,
            "Grid": QGridLayout,
            "Form": QFormLayout,
            "Stacked": QStackedLayout,
        }.get(layout_type, QVBoxLayout)()

    @staticmethod
    def margins_handler(
        parent: QWidget, margins: Optional[Tuple[int, int, int, int]] = None
    ) -> Tuple[int, int, int, int]:
        """
        Initialize the MarginsHandler with a specified margins.

        Args:
            margins (Tuple[int, int, int, int]): Margins for a layout.
                Default is parent's margins.

        Returns:
            Tuple[int, int, int, int]: A tuple of margins.
        """
        pmargins = parent.contentsMargins()
        return (
            margins
            if margins is not None
            and all(isinstance(i, int) for i in margins)
            and len(margins) == 4
            else (pmargins.left(), pmargins.top(), pmargins.right(), pmargins.bottom())
        )
