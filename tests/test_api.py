from unittest.mock import patch

import requests

from src.api import NominatimAPI, OpenSkyAPI


def test_nominatim_get_data():
    """Проверяет получение координат, границ страны."""
    boundingbox = ["36.0", "43.0", "-9.0", "3.0"]
    with patch("src.api.requests.get") as mock_get:
        mock_get.return_value.json.return_value = [{"boundingbox": boundingbox}]
        api = NominatimAPI("Spain")
        result = api.get_data()

    assert result == boundingbox


def test_opensky_get_data():
    """Проверяет получение данных о воздушных судах их OpenSky API."""
    boundingbox = ["36.0", "43.0", "-9.0", "3.0"]
    expected_data = {"time": 123456, "states": [["abc123", "AFL123"]]}

    with patch("src.api.requests.get") as mock_get:
        mock_get.return_value.json.return_value = expected_data
        api = OpenSkyAPI(boundingbox)
        result = api.get_data()
    assert result == expected_data


def test_nominatim_connection_error():
    """Проверяет обработку ошибки подключения."""
    with patch("src.api.requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.RequestException
        api = NominatimAPI("Spain")

        try:
            api.get_data()
        except ConnectionError as error:
            assert str(error) == "Ошибка подключения к Nominatim API"
        else:
            assert False, "Ожидалась ошибка ConnectionError"


def test_nominatim_country_not_found():
    """Проверяет ситуацию, когда страна не найдена."""
    with patch("src.api.requests.get") as mock_get:
        mock_get.return_value.json.return_value = []

        api = NominatimAPI("UnknownCountry")

        try:
            api.get_data()
        except ValueError as error:
            assert str(error) == "Страна не найдена"
        else:
            assert False, "Ожидалась ошибка ValueError"


def test_nominatim_invalid_response():
    """Проверяет обработку ответа без boundingbox."""
    with patch("src.api.requests.get") as mock_get:
        mock_get.return_value.json.return_value = [{"name": "Spain"}]

        api = NominatimAPI("Spain")

        try:
            api.get_data()
        except ValueError as error:
            assert str(error) == "Некорректный ответ Nominatim API"
        else:
            assert False, "Ожидалась ошибка ValueError"


def test_opensky_connection_error():
    """Проверяет обработку ошибки подключения."""
    with patch("src.api.requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.RequestException

        api = OpenSkyAPI([1, 2, 3, 4])

        try:
            api.get_data()
        except ConnectionError as error:
            assert str(error) == "Ошибка подключения к OpenSky API"
        else:
            assert False, "Ожидалась ошибка ConnectionError"


def test_opensky_invalid_response():
    """Проверяет обработку некорректного ответа OpenSky."""
    with patch("src.api.requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"time": 123456}

        api = OpenSkyAPI([1, 2, 3, 4])

        try:
            api.get_data()
        except ValueError as error:
            assert str(error) == "Некорректный ответ OpenSky API"
        else:
            assert False, "Ожидалась ошибка ValueError"
