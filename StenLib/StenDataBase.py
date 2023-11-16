import json
from pathlib import Path
from typing import Any


class DataBase:
    """A class for managing JSON files."""

    def __init__(self, file_name: str, data_folder: str = "data") -> None:
        """Initialize the DataBase class.

        Args:
            file_name (str): The name of the JSON file.
            data_folder (str, optional): The name of the data folder. Defaults to "data".
        """
        file_path = self.data_path_generator(data_folder) / file_name
        self.file_path = Path(file_path)
        if not self.file_path.is_file():
            self.data = {}
        else:
            with self.file_path.open("r") as f:
                self.data = json.load(f)

    def get(self, key: str) -> Any:
        """Get the value for a key.

        Args:
            key (str): The key to get the value for.
        """
        return self.data.get(key)

    def set(self, key: str, value: Any) -> None:
        """Set the value for a key.

        Args:
            key (str): The key to set the value for.
            value (Any): The value to set.
        """
        self.data[key] = value

    def delete(self, key: str) -> None:
        """Delete a key.

        Args:
            key (str): The key to delete.
        """
        if key in self.data:
            del self.data[key]

    def save(self) -> None:
        """Save the data to the file."""
        with self.file_path.open("w") as f:
            json.dump(self.data, f)

    @staticmethod
    def data_path_generator(data_folder: str = "data") -> Path:
        """Create the data path.

        Args:
            data_folder (str, optional):
                The name of the data folder. Defaults to "data".

        Returns:
            str: The path to the data directory.
        """
        data_path = Path(__file__).parent / data_folder
        data_path.mkdir(parents=True, exist_ok=True)
        return data_path
