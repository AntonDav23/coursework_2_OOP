from src.aeroplane import Aeroplane


def convert_to_aircraft(data: list[list]) -> list[Aeroplane]:
    """Преобразует данные API в список объектов Aeroplane."""
    aircraft_list = []
    for aircraft_data in data:
        if not aircraft_data:
            continue
        aircraft = Aeroplane(
            icao24=aircraft_data[0],
            callsign=aircraft_data[1],
            origin_country=aircraft_data[2],
            longitude=aircraft_data[5],
            latitude=aircraft_data[6],
            baro_altitude=aircraft_data[7],
            velocity=aircraft_data[9],
            true_track=aircraft_data[10],
        )
        aircraft_list.append(aircraft)
    return aircraft_list


def filter_by_country(aircraft_list: list[Aeroplane], country: str) -> list[Aeroplane]:
    """Фильтрует самолеты по стране регистрации."""
    filtered_list = []
    for aircraft in aircraft_list:
        if aircraft.origin_country == country:
            filtered_list.append(aircraft)
    return filtered_list


def sort_by_altitude(aircraft_list: list[Aeroplane]) -> list[Aeroplane]:
    """Сортирует самолеты по высоте полета."""
    return sorted(aircraft_list, key=lambda aircraft: aircraft.baro_altitude or 0, reverse=True)


def get_top_aircraft(aircraft_list: list[Aeroplane], count: int) -> list[Aeroplane]:
    """Возвращает заданное количество самолетов с наибольшей высотой."""
    sorted_list = sort_by_altitude(aircraft_list)
    return sorted_list[:count]
