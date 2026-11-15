from requests.exceptions import RequestException

from src.api import NominatimAPI, OpenSkyAPI
from src.json_saver import JsonSaver
from src.utils import convert_to_aircraft


def main() -> None:
    country = input("Введите название страны на английском языке: ").strip()
    if not country:
        print("Название страны не может быть пустым.")
        return

    try:
        nominatim = NominatimAPI(country)
        boundingbox = nominatim.get_data()

        api = OpenSkyAPI(boundingbox)
        result = api.get_data()
        aircraft_list = convert_to_aircraft(result["states"])

        print(f"Найдено самолетов над страной {country}: {len(aircraft_list)}")

        saver = JsonSaver("src/aircraft.json")
        saver.save(aircraft_list)
        print("Данные успешно сохранены.")

    except (ConnectionError, RequestException) as error:
        print(f"Ошибка подключения: {error}")

    except ValueError as error:
        print(f"Ошибка обработки данных: {error}")


if __name__ == "__main__":
    main()
