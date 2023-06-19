from collections import namedtuple
import typing
from typing import NamedTuple

Coordinate = namedtuple('Coordinate', 'lat lon')
issubclass(Coordinate, tuple)
moscow = Coordinate(55.756, 37.617)

print(moscow)

print(moscow == Coordinate(lat=55.756, lon=37.617))

# Similar thing but with typing

Coordinate = typing.NamedTuple('Coordinate', [('lat', float), ('lon', float)])

print(issubclass(Coordinate, tuple))

# Same to __dict__
print(typing.get_type_hints(Coordinate))


class Coordinate(NamedTuple):
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'
