from abc import ABC, abstractmethod
from typing import Any


class DBConnection(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def disconnect(self) -> None:
        pass

    @abstractmethod
    def commit(self) -> None:
        pass

    @abstractmethod
    def execute_query(self, query: str, params: tuple[Any, ...]) -> None:
        pass

    @abstractmethod
    def fetch_one(self, query: str, params: tuple[Any, ...]) -> dict[str, Any]:
        pass
