class Aeroplane:
    def __init__(
        self,
        icao24: str,
        callsign: str | None,
        origin_country: str,
        longitude: float | None,
        latitude: float | None,
        baro_altitude: float | None,
        velocity: float | None,
        true_track: float | None,
    ) -> None:
        if not icao24 or not origin_country:
            raise ValueError("Не указаны обязательные данные самолета")
        # if baro_altitude is not None and baro_altitude < 0:
        #    raise ValueError("Высота не может быть отрицательной")
        if velocity is not None and velocity < 0:
            raise ValueError("Скорость не может быть отрицательной")
        if latitude is not None and not -90 <= latitude <= 90:
            raise ValueError("Некорректная широта")
        if longitude is not None and not -180 <= longitude <= 180:
            raise ValueError("Некорректная долгота")
        self.icao24 = icao24
        self.callsign = callsign
        self.origin_country = origin_country
        self.longitude = longitude
        self.latitude = latitude
        self.baro_altitude = baro_altitude
        self.velocity = velocity
        self.true_track = true_track

    def __gt__(self, other: "Aeroplane") -> bool:
        if self.velocity is not None and other.velocity is not None:
            return self.velocity > other.velocity
        return False

    def __lt__(self, other: "Aeroplane") -> bool:
        if self.velocity is not None and other.velocity is not None:
            return self.velocity < other.velocity
        return False

    def __ge__(self, other: "Aeroplane") -> bool:
        if self.baro_altitude is not None and other.baro_altitude is not None:
            return self.baro_altitude >= other.baro_altitude
        return False

    def __le__(self, other: "Aeroplane") -> bool:
        if self.baro_altitude is not None and other.baro_altitude is not None:
            return self.baro_altitude <= other.baro_altitude
        return False

    def __str__(self) -> str:
        return f"Самолет: {self.callsign}, страна: {self.origin_country}, скорость: {self.velocity} м/с"

    def __repr__(self) -> str:
        return f"Борт: {self.icao24}, Самолет: {self.callsign}, страна: {self.origin_country}"
