from typing import Any

class QeHelper:
    CHARS: str
    @staticmethod
    def alphanumeric_id_generator(
        char_len: int = 6, use_secrets: bool = False
    ) -> str: ...
    @staticmethod
    def data_path_generator() -> str: ...
    @staticmethod
    def stringification(data: Any) -> str: ...
    @staticmethod
    def destringification(data: str) -> Any: ...
