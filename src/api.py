from typing import Any

import requests

from src.base_api import BaseAPI


class NominatimAPI(BaseAPI):
    url = "https://nominatim.openstreetmap.org/search"
    headers = {"User-Agent": "Coursework2-AircraftApp/1/0"}

    def __init__(self, country: str) -> None:
        self.country = country
        self.params: dict = {
            "country": self.country,
            "format": "jsonv2",
            "addressdetails": 1,
        }

    def get_data(self) -> Any:
        try:
            response = requests.get(
                self.url,
                params=self.params,
                headers=self.headers,
                timeout=10,
            )
            response.raise_for_status()
        except requests.exceptions.RequestException as error:
            raise ConnectionError("Ошибка подключения к Nominatim API") from error

        data = response.json()
        if not data:
            raise ValueError("Страна не найдена")
        try:
            boundingbox = data[0]["boundingbox"]
        except IndexError, KeyError, TypeError:
            raise ValueError("Некорректный ответ Nominatim API")
        return boundingbox


class OpenSkyAPI(BaseAPI):
    """Класс для получения данных о воздушных судах."""

    url = "https://opensky-network.org/api/states/all"

    def __init__(self, boundingbox: list) -> None:
        self.boundingbox = boundingbox
        self.params = {
            "lamin": self.boundingbox[0],
            "lamax": self.boundingbox[1],
            "lomin": self.boundingbox[2],
            "lomax": self.boundingbox[3],
        }

    def get_data(self) -> Any:
        try:
            response = requests.get(
                self.url,
                params=self.params,
                timeout=10,
            )
            response.raise_for_status()
        except requests.exceptions.RequestException as error:
            raise ConnectionError("Ошибка подключения к OpenSky API") from error
        data = response.json()
        if not isinstance(data, dict) or "states" not in data:
            raise ValueError("Некорректный ответ OpenSky API")
        return data
