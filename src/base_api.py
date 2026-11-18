from abc import ABC, abstractmethod
from typing import Any


class BaseAPI(ABC):
    """Абстрактный класс для работы с API."""

    @abstractmethod
    def get_data(self) -> Any:
        """Получение данных из API."""
        pass
