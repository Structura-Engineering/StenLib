from enum import Enum
from typing import Type, Union


class EnumUtils(Enum):
    """A class that contains core methods for Enum."""

    @classmethod
    def get_all_values(cls) -> list[Union[Enum, Type]]:
        """
        Get all values of an Enum class as a list.

        Args:
            enum_class (Type[Enum]): The Enum class.

        Returns:
            list[Union[Enum, Type]]: A list of enum values.
        """
        return list(cls.__members__.values())
