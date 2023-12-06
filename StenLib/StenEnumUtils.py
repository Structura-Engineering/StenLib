from enum import Enum


class EnumUtils(Enum):
    """A class that contains core methods for Enum."""

    @classmethod
    def get_all_values(cls) -> list[Enum | type]:
        """
        Get all values of an Enum class as a list.

        Returns:
            list[Enum | type]: A list of all values of the Enum class.

        Example:
            >>> class ExampleEnum(EnumUtils):
            ...     A = 1
            ...     B = 2
            ...     C = 3
            >>> ExampleEnum.get_all_values()
            [<ExampleEnum.A: 1>, <ExampleEnum.B: 2>, <ExampleEnum.C: 3>]
        """
        return list(cls.__members__.values())
