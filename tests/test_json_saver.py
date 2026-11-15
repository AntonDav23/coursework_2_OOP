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


def test_add(tmp_path):
    """Проверяет добавление самолета в JSON."""
    filename = tmp_path / "test_aircraft.json"
    plane = Aeroplane("abc123", "AFL123", "Russia", 37.6, 55.7, 10000.0, 250.0, 180.0)
    saver = JsonSaver(filename)
    saver.add(plane)

    with open(filename, encoding="utf-8") as file:
        data = json.load(file)

    assert len(data) == 1
    assert data[0]["icao24"] == "abc123"
    assert data[0]["callsign"] == "AFL123"


def test_delete(tmp_path):
    """Проверяет удаление самолета из JSON."""
    filename = tmp_path / "test_aircraft.json"
    plane = Aeroplane("abc123", "AFL123", "Russia", 37.6, 55.7, 10000.0, 250.0, 180.0)
    saver = JsonSaver(filename)
    saver.add(plane)
    saver.delete("abc123")

    with open(filename, encoding="utf-8") as file:
        data = json.load(file)

        assert data == []


def test_get(tmp_path):
    """Проверяет удаление самолета из JSON."""
    filename = tmp_path / "test_aircraft.json"
    plane = Aeroplane("abc123", "AFL123", "Russia", 37.6, 55.7, 10000.0, 250.0, 180.0)
    saver = JsonSaver(filename)
    saver.add(plane)

    result = saver.get("abc123")

    assert result["icao24"] == "abc123"
    assert result["callsign"] == "AFL123"


def test_get_not_found(tmp_path):
    """Проверяет поиск отсутствующего самолета ."""
    filename = tmp_path / "test_aircraft.json"
    saver = JsonSaver(filename)
    saver.save([])

    result = saver.get("unknown")

    assert result is None
