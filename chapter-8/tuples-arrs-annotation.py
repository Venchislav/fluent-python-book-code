from geolib import geohash as gh  # type: ignore
from typing import NamedTuple

PRECISION = 9


# Means that these two elems of attr must be float


def geohash(lat_lon: tuple[float, float]) -> str:
    return gh.encode(*lat_lon, PRECISION)


# We can also use NamedTuple as annotation

class Coordinate(NamedTuple):
    lat: float
    lon: float


def geohash(lat_lon: Coordinate) -> str:
    return gh.encode(*lat_lon, PRECISION)
