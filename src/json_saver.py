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

    def add(self, aircraft: Any) -> None:
        """Добавляет самолет в JSON."""
        try:
            with open(self.filename, encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        data.append(vars(aircraft))
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def get(self, icao24: str) -> Any:
        """Находит самолет по идентификатору."""
        with open(self.filename, encoding="utf-8") as file:
            data = json.load(file)
        for aircraft in data:
            if aircraft["icao24"] == icao24:
                return aircraft
        return None

    def delete(self, icao24: str) -> None:
        """Удаляет самолет по идентификатору."""
        with open(self.filename, encoding="utf-8") as file:
            data = json.load(file)
        data = [aircraft for aircraft in data if aircraft["icao24"] != icao24]
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
