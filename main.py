from requests.exceptions import RequestException

from src.api import NominatimAPI, OpenSkyAPI
from src.json_saver import JsonSaver
from src.utils import convert_to_aircraft, filter_by_country, get_top_aircraft


def main() -> None:
    country = input("Введите название страны на английском языке: ").strip()
    if not country:
        print("Название страны не может быть пустым.")
        return

    try:
        count = int(input("Сколько самолетов показать в топе: "))
        if count <= 0:
            print("Количество должно быть больше нуля.")
            return
    except ValueError:
        print("Введите целое положительное число.")
        return

    try:
        nominatim = NominatimAPI(country)
        boundingbox = nominatim.get_data()

        api = OpenSkyAPI(boundingbox)
        result = api.get_data()
        aircraft_list = convert_to_aircraft(result["states"])
        top_aircraft = get_top_aircraft(aircraft_list, count)

        registration_country = input("Введите страну регистрации самолетов на английском языке: ").strip()
        if not registration_country:
            print("Название страны регистрации не может быть пустым.")
            return

        filtered_aircraft = filter_by_country(aircraft_list, registration_country)

        print(f"Найдено самолетов над страной {country}: {len(aircraft_list)}")
        print(f"\nТоп {count} самолетов по высоте:")

        for aircraft in top_aircraft:
            print(aircraft)

        print(f"\nСамолеты страны регистрации {registration_country}:")

        if filtered_aircraft:
            for aircraft in filtered_aircraft:
                print(aircraft)
        else:
            print("Самолеты этой страны не найдены.")

        saver = JsonSaver("src/aircraft.json")
        saver.save(aircraft_list)
        print("Данные успешно сохранены.")

    except (ConnectionError, RequestException) as error:
        print(f"Ошибка подключения: {error}")

    except ValueError as error:
        print(f"Ошибка обработки данных: {error}")


if __name__ == "__main__":
    main()
