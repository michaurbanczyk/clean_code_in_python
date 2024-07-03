from dataclasses import dataclass


@dataclass
class Point:
    lat: float
    long: float


def locate(latitude: float, longitude: float) -> Point:
    """Find and object in the map by its coordinates"""


print(locate.__annotations__)
