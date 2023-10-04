import json
from typing import Dict, List


class QeDataBase:
    """
    A class for reading and writing data to a JSON file.

    Attributes:
        None

    Methods:
        write_to_json(cls, data: Dict[str, List[List[int]]], file_path: str) -> None:
            Writes data to a JSON file.

        read_from_json(cls, file_path: str) -> Dict[str, List[List[int]]]:
            Retrieves data from a JSON file.
    """

    @classmethod
    def write(cls, data: Dict[str, List[List[int]]], file_path: str) -> None:
        """
        Writes data to a JSON file.

        Args:
            data (Dict[str, List[List[int]]]): The data to be written in dictionary format.
            file_path (str): The path of the JSON file.

        Returns:
            None
        """
        with open(file_path, "w") as json_file:
            json.dump(data, json_file)

    @classmethod
    def read(cls, file_path: str) -> Dict[str, List[List[int]]]:
        """
        Retrieves data from a JSON file.

        Args:
            file_path (str): The path of the JSON file.

        Returns:
            Dict[str, List[List[int]]]: The data retrieved in dictionary format.
        """
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
        return data

    @classmethod
    def create(cls, file_path: str) -> None:
        """
        Creates a JSON file.

        Args:
            file_path (str): The path of the JSON file.

        Returns:
            None
        """
        with open(file_path, "w") as json_file:
            json.dump({}, json_file)

    @classmethod
    def delete(cls, file_path: str) -> None:
        """
        Deletes a JSON file.

        Args:
            file_path (str): The path of the JSON file.

        Returns:
            None
        """
        import os

        os.remove(file_path)
