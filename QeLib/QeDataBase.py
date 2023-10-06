import json
import os
from pathlib import Path
from typing import Dict, List, Optional, Union

from QeHelper import QeHelper


class QeDataBase(QeHelper):
    """A class for managing JSON files."""

    @classmethod
    def load(
        cls, file_name: Optional[Union[str, None]] = None
    ) -> Union[List[Path], Path]:
        """
        Load data from a JSON file.

        Args:
            file_name (str, optional):
                The name of the file (without extension). Defaults to None.

        Returns:
            Union[List[Path], Path]: If file_name is None,
                returns a list of Path objects for all JSON files in the directory.
            If file_name is provided, returns the Path to the specific file.
        """
        data_dir: Path = Path(cls.data_path_generator())
        if file_name:
            return data_dir / f"{file_name}.json"
        return [
            data_dir / filename
            for filename in os.listdir(data_dir)
            if filename.endswith(".json")
        ]

    @classmethod
    def write(cls, data: Dict, file_name: str) -> None:
        """
        Write data to a JSON file.

        Args:
            data (dict): The data to write.
            file_name (str): The name of the file (without extension).
        """
        with open(str(cls.load(file_name)), "w") as json_file:
            json.dump(data, json_file)

    @classmethod
    def read(cls, file_name: Optional[Union[str, None]] = None) -> Dict:
        """
        Read data from a JSON file.

        Args:
            file_name (str, optional):
                The name of the file (without extension). Defaults to None.
                    if None loads all files.

        Returns:
            dict: The data from the file.
        """
        data: Dict = {}
        file_path = cls.load(file_name)
        if isinstance(file_path, list):
            for filename in file_path:
                with open(filename, "r") as json_file:
                    data.update(json.load(json_file))
        else:
            with open(file_path, "r") as json_file:
                data = json.load(json_file)
        return data

    @classmethod
    def create(cls, file_name: str) -> None:
        """
        Create a new JSON file.

        Args:
            file_name (str): The name of the file (without extension).
        """
        with open(str(cls.load(file_name)), "w") as json_file:
            json.dump({}, json_file)

    @classmethod
    def delete(cls, file_name: str) -> None:
        """
        Delete a JSON file.

        Args:
            file_name (str): The name of the file (without extension).
        """
        os.remove(str(cls.load(file_name)))
