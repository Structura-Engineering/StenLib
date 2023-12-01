from enum import Enum
from typing import Type, Union


class EnumUtils(Enum):
    """A class that contains core methods for Enum."""

    @classmethod
    def get_all_values(cls) -> list[Union[Enum, Type]]:
        """
        Get all values of an Enum class as a list.

        Returns:
            list[Union[Enum, Type]]: A list of enum values.

        Example:
            >>> class ExampleEnum(Enum):
            ...     A = 1
            ...     B = 2
            ...     C = 3
            >>> ExampleEnum.get_all_values()
            [<ExampleEnum.A: 1>, <ExampleEnum.B: 2>, <ExampleEnum.C: 3>]
        """
        return list(cls.__members__.values())
