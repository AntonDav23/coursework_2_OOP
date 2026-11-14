from src.aeroplane import Aeroplane


def test_create_aeroplane():
    """Проверяет создание объекта самолета и заполнение его атрибутовю"""
    plane = Aeroplane(
        icao24="abc123",
        callsign="AFL123",
        origin_country="Russia",
        longitude=37.6,
        latitude=55.7,
        baro_altitude=10000.0,
        velocity=250.0,
        true_track=180.0,
    )
    assert plane.icao24 == "abc123"
    assert plane.callsign == "AFL123"
    assert plane.origin_country == "Russia"


def test_compare_by_speed():
    """Проверяет сравнение двух самолетов по скорости"""
    plane1 = Aeroplane("abc123", "AFL123", "Russia", 37.6, 55.7, 10000.0, 250.0, 180.0)
    plane2 = Aeroplane("abc456", "AFL456", "Russia", 37.7, 55.8, 11000.0, 200.0, 190.0)

    assert plane1 > plane2
    assert plane2 < plane1


def test_compare_by_altitude():
    """Проверяет сравнение двух самолетов по скорости"""
    plane1 = Aeroplane("abc123", "AFL123", "Russia", 37.6, 55.7, 12000.0, 250.0, 180.0)
    plane2 = Aeroplane("abc456", "AFL456", "Russia", 37.7, 55.8, 10000.0, 200.0, 190.0)

    assert plane1 > plane2
    assert plane2 < plane1


def test_str():
    """Проверяет строковое представление объекта самолета."""
    plane = Aeroplane("abc123", "AFL123", "Russia", 37.6, 55.7, 10000.0, 250.0, 180.0)

    assert str(plane) == "Самолет: AFL123, страна: Russia, скорость: 250.0 м/с"


def test_repr():
    """Проверяет техническое представление объекта самолета."""
    plane = Aeroplane("abc123", "AFL123", "Russia", 37.6, 55.7, 10000.0, 250.0, 180.0)

    assert repr(plane) == "Борт: abc123, Самолет: AFL123, страна: Russia"


def test_compare_when_values_are_none():
    """Проверяет сравнение самолетов при отсутствии скорости или высоты"""
    plane1 = Aeroplane("abc123", "AFL123", "Russia", None, None, None, None, None)
    plane2 = Aeroplane("abc456", "AFL456", "Russia", 37.6, 55.7, 10000.0, 250.0, 180.0)
    assert not (plane1 > plane2)
    assert not (plane1 < plane2)
    assert not (plane1 >= plane2)
    assert not (plane1 <= plane2)
