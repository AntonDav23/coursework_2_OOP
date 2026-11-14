import json

from src.aeroplane import Aeroplane
from src.json_saver import JsonSaver


def test_save(tmp_path):
    """Проверяет сохранение списка самолетов в JSON."""
    filename = tmp_path / "test_aircraft.json"
    plane = Aeroplane("abc123", "AFL123", "Russia", 37.6, 55.7, 10000.0, 250.0, 180.0)
    saver = JsonSaver(filename)
    saver.save([plane])

    with open(filename, encoding="utf-8") as file:
        data = json.load(file)

    assert data[0]["icao24"] == "abc123"
    assert data[0]["callsign"] == "AFL123"
    assert data[0]["origin_country"] == "Russia"
