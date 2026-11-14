from unittest.mock import patch

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
