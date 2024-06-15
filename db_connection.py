from abc import ABC, abstractmethod
from typing import Any


class DBConnection(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def create(self, table: str, data: dict[str, Any]) -> None:
        pass

    @abstractmethod
    def read(self, table: str, query: dict[str, Any]) -> list[dict[str, Any]]:
        pass

    @abstractmethod
    def update(self, table: str, query: dict[str, Any], data: dict[str, Any]) -> None:
        pass

    @abstractmethod
    def execute_query(self, query: str, params: tuple[Any, ...]) -> None:
        pass

    @abstractmethod
    def fetch_all(self, query: str, params: tuple[Any, ...]) -> list[dict[str, Any]]:
        pass
