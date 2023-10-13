from enum import Enum
from typing import List, Type, Union


class EnumUtils(Enum):
    """A class that contains core methods for Enum."""

    @classmethod
    def get_all_values(cls) -> List[Union[Enum, Type]]:
        """
        Get all values of an Enum class as a list.

        Args:
            enum_class (Type[Enum]): The Enum class.

        Returns:
            List[Union[Enum, Type]]: A list of enum values.
        """
        return list(cls.__members__.values())
