# public, private


class Connector:

    def __init__(self, source):
        self.source = source
        self._timeout = 60
        self.__private_timeout = 30


conn = Connector("localhost")
print(conn._timeout)
print(conn._Connector__private_timeout)


# setters and getters
class Coordinate:
    def __init__(self, lat: float, long: float) -> None:
        self._latitude = self._longitude = None
        self.latitude = lat
        self.longitude = long

    @property
    def latitude(self) -> float:
        return self._latitude

    @latitude.setter
    def latitude(self, lat_value: float) -> None:
        if lat_value not in range(-90, 90 + 1):
            raise ValueError(f"{lat_value} is an invalid value for latitude")
        self._latitude = lat_value

    @property
    def longitude(self) -> float:
        return self._longitude

    @longitude.setter
    def longitude(self, long_value: float) -> None:
        if long_value not in range(-180, 180 + 1):
            raise ValueError(f"{long_value} is an invalid value for longitude")
        self._longitude = long_value


new_coordinate = Coordinate(20, 44)
print(new_coordinate.latitude)
print(new_coordinate.longitude)

new_coordinate.latitude = 50
print(new_coordinate.latitude)
