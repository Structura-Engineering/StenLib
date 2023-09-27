from typing import Iterable, Union

class QeLoadedData:
    def __init__(self, data: dict[str, list[list[int]]]) -> None: ...
    def __getattr__(self, key: str) -> Union[list[list[int]], None]: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __iter__(self) -> Iterable[str]: ...

class QeBaseClass:
    @staticmethod
    def data_path() -> str: ...
    @classmethod
    def load_data(cls) -> None: ...