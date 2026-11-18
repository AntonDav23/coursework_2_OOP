from abc import ABC, abstractmethod
from typing import Any


class BaseSaver(ABC):
    """Абстрактный Класс для сохранения данных."""

    @abstractmethod
    def save(self, data: Any) -> None:
        """Сохраняет данные."""
        pass

    @abstractmethod
    def add(self, aircraft: Any) -> None:
        """Добавляет самолет."""
        pass

    @abstractmethod
    def get(self, icao24: str) -> Any:
        """Находит самолет по идентификатору."""
        pass

    @abstractmethod
    def delete(self, icao24: str) -> None:
        """Удаляет самолет по идентификатору."""
        pass
