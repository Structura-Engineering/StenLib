import json
import os
from typing import Dict, Iterable, List, Union


class QeLoadedData:
    """
    Represents loaded data for QE.

    Attributes:
        data (Dict[str, List[List[int]]]): The loaded data.

    Methods:
        __getattr__(key: str) -> Union[List[List[int]], None]:
            Get the value associated with the key.
        __str__() -> str: Return a string representation of the loaded data.
        __repr__() -> str: Return a string representation of the loaded data.
        __iter__() -> Iterable[str]: Return an iterator over the keys.
    """

    def __init__(self, data: Dict[str, List[List[int]]]) -> None:
        """
        Initialize with loaded data.

        Args:
            data (Dict[str, List[List[int]]]): The loaded data.
        """
        self.data = data

    def __getattr__(self, key: str) -> Union[List[List[int]], None]:
        """
        Get the value associated with the key.

        Args:
            key (str): The key.

        Returns:
            Union[List[List[int]], None]:
                The value associated with the key, or None if not found.
        """
        return self.data.get(key)

    def __str__(self) -> str:
        """
        Return a string representation of the loaded data.

        Returns:
            str: The string representation of the loaded data.
        """
        return str(self.data)

    def __repr__(self) -> str:
        """
        Return a string representation of the loaded data.

        Returns:
            str: The string representation of the loaded data.
        """
        return repr(self.data)

    def __iter__(self) -> Iterable[str]:
        """
        Return an iterator over the keys.

        Returns:
            Iterable[str]: An iterator over the keys.
        """
        return iter(self.data)


class QeBaseClass:
    """
    Base class for QE.

    Methods:
        data_path() -> str: Get the data path.
        load_data() -> None: Load data for QE.
    """

    def __init__(self) -> None:
        """Initialize QeBaseClass and load data."""
        super().__init__()
        self.load_data()

    @staticmethod
    def data_path() -> str:
        """
        Get the data path.

        Returns:
            str: The data path.
                If the path does not exist, it will be created.
        """
        path = os.path.abspath(os.path.join("QeLib", "data"))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        return path

    @classmethod
    def load_data(cls) -> None:
        """Load data for QE."""
        for filename in os.listdir(QeBaseClass.data_path()):
            with open(os.path.join(QeBaseClass.data_path(), filename), "r") as file:
                data = json.load(file)
                attr_name = filename.split(".")[0].upper().replace("_", "")
                loaded_data = QeLoadedData(data)
                setattr(cls, attr_name, loaded_data)

    # TODO: Make sure you can add/remove anything not just lists.

    @classmethod
    def add_data(cls, key: str) -> None:
        """
        Add data for QE.

        Args:
            key (str): The key.
        """

    @classmethod
    def remove_data(cls, key: str) -> None:
        """
        Remove data for QE.

        Args:
            key (str): The key.
        """
