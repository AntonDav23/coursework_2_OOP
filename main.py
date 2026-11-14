from src.api import NominatimAPI, OpenSkyAPI
from src.json_saver import JsonSaver
from src.utils import convert_to_aircraft


def main() -> None:
    country = "Spain"
    nominatim = NominatimAPI(country)
    boundingbox = nominatim.get_data()

    api = OpenSkyAPI(boundingbox)
    result = api.get_data()
    aircraft_list = convert_to_aircraft(result["states"])
    print(len(aircraft_list))

    saver = JsonSaver("src/aircraft.json")
    saver.save(aircraft_list)


if __name__ == "__main__":
    main()
