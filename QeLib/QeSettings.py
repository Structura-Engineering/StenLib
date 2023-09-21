from typing import List, Tuple

from QeBaseClass import QeBaseClass


class LumberTypes(QeBaseClass):
    """
    A class to represent different types of lumber.

    This class provides definitions for various types of lumber commonly used in construction projects.
    It categorizes the lumber into two main classes: SLS (Standard Lumber Sizes) and CLS (Custom Lumber Sizes).

    Attributes:
        SLS (list[tuple[int, int]]): A list of tuples representing dimensions of Standard Lumber Sizes.
            Each tuple contains two integers: the width (in mm) and height (in mm) of the lumber.
        CLS (list[tuple[int, int]]): A list of tuples representing dimensions of Custom Lumber Sizes.
            Each tuple contains two integers: the width (in mm) and height (in mm) of the lumber.

    Methods:
        getattr(): Retrieves non-callable attributes of the class. Inherent from QeBaseClass.

    Example Usage:
        >>> print(LumberTypes.SLS)
        [(38, 89), (38, 120), (38, 140), (38, 170), (38, 184), (38, 235), (38, 285)]
        >>> print(LumberTypes.CLS)
        [(50, 75), (50, 100), (50, 125), (50, 150), (50, 175)]
    """

    SLS: List[Tuple[int, int]] = [
        (38, 89),
        (38, 120),
        (38, 140),
        (38, 170),
        (38, 184),
        (38, 235),
        (38, 285),
    ]

    CLS: List[Tuple[int, int]] = [
        (50, 75),
        (50, 100),
        (50, 125),
        (50, 150),
        (50, 175),
    ]


print(LumberTypes.getattr())
