import json
from typing import Any

from src.base_saver import BaseSaver


class JsonSaver(BaseSaver):
    """Класс для сохранения данных в JSON."""

    def __init__(self, filename: str = "aircraft.json") -> None:
        self.filename = filename

    def save(self, data: Any) -> None:
        """Сохраняет данные в JSON"""
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump([vars(aircraft) for aircraft in data], file, ensure_ascii=False, indent=4)
