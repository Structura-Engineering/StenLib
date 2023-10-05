import json
import os
from typing import Dict, List

from QeHelper import QeHelper


class QeDataBase(QeHelper):
    """A class for handling JSON data files related to QeHelper."""

    @classmethod
    def get_json_file_path(cls, file_name: str) -> str:
        """
        Generate the file path for a JSON file.

        Args:
            file_name (str): The name of the JSON file.

        Returns:
            str: The full file path.
        """
        return os.path.join(cls.data_path_generator(), f"{file_name}.json")

    @classmethod
    def write(cls, data: Dict[str, List[List[int]]], file_name: str) -> None:
        """
        Write data to a JSON file.

        Args:
            data (Dict[str, List[List[int]]]): The data to be written.
            file_name (str): The name of the JSON file.
        """
        with open(cls.get_json_file_path(file_name), "w") as json_file:
            json.dump(data, json_file)

    @classmethod
    def read(cls, file_name: str) -> Dict[str, List[List[int]]]:
        """
        Read data from a JSON file.

        Args:
            file_name (str): The name of the JSON file.

        Returns:
            Dict[str, List[List[int]]]: The read data.
        """
        with open(cls.get_json_file_path(file_name), "r") as json_file:
            data = json.load(json_file)
        return data

    @classmethod
    def create(cls, file_name: str) -> None:
        """
        Create a new JSON file.

        Args:
            file_name (str): The name of the JSON file.
        """
        with open(cls.get_json_file_path(file_name), "w") as json_file:
            json.dump({}, json_file)

    @classmethod
    def delete(cls, file_name: str) -> None:
        """
        Delete a JSON file.

        Args:
            file_name (str): The name of the JSON file to be deleted.
        """
        os.remove(cls.get_json_file_path(file_name))
