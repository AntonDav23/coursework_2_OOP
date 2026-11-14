from src.aeroplane import Aeroplane
from src.utils import convert_to_aircraft, filter_by_country, get_top_aircraft, sort_by_altitude


def test_convert_to_aircraft():
    """Проверяет преобразование данных API в объекты самолетов."""
    data = [["abc123", "AFL123", "Russia", None, None, 37.6, 55.7, 10000.0, None, 250.0, 180.0]]
    aircraft = convert_to_aircraft(data)
    assert len(aircraft) == 1
    assert aircraft[0].icao24 == "abc123"
    assert aircraft[0].callsign == "AFL123"
    assert aircraft[0].origin_country == "Russia"
    assert aircraft[0].baro_altitude == 10000.0


def test_filter_by_country():
    """Проверяет фильтрацию самолетов по стране."""
    data = [
        Aeroplane("abc123", "AFL123", "Russia", 37.6, 55.7, 10000.0, 250.0, 180.0),
        Aeroplane("def456", "BAW456", "France", 2.3, 48.8, 9000.0, 230.0, 170.0),
    ]
    result = filter_by_country(data, "Russia")
    assert len(result) == 1
    assert result[0].origin_country == "Russia"


def test_sort_by_altitude():
    """Проверяет сортировку самолетов по высоте."""
    plane1 = Aeroplane("abc123", "AFL123", "Russia", 37.6, 55.7, 8000.0, 250.0, 180.0)
    plane2 = Aeroplane("def456", "BAW456", "France", 2.3, 48.8, 12000.0, 230.0, 170.0)
    plane3 = Aeroplane("ghi789", "DLH789", "Germany", 13.4, 52.2, 10000.0, 240.0, 175.0)
    aircraft_list = [plane1, plane2, plane3]

    result = sort_by_altitude(aircraft_list)

    assert len(result) == 3
    assert result[0] is plane2
    assert result[1] is plane3
    assert result[2] is plane1


def test_get_top_aircraft():
    """Проверяет получение заданного количества самолетов с наибольшей высотой."""
    plane1 = Aeroplane("abc123", "AFL123", "Russia", 37.6, 55.7, 8000.0, 250.0, 180.0)
    plane2 = Aeroplane("def456", "BAW456", "France", 2.3, 48.8, 12000.0, 230.0, 170.0)
    plane3 = Aeroplane("ghi789", "DLH789", "Germany", 13.4, 52.2, 10000.0, 240.0, 175.0)

    result = get_top_aircraft([plane1, plane2, plane3], 2)

    assert len(result) == 2
    assert result[0] is plane2
    assert result[1] is plane3
