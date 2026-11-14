from abc import ABC, abstractmethod
from typing import Any


class BaseSaver(ABC):
    """Абстрактный Класс для сохранения данных."""

    @abstractmethod
    def save(self, data: Any) -> None:
        """Сохраняет данные."""
        pass
