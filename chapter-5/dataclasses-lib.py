from dataclasses import dataclass


@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


# However:

# These are classes that have fields, methods for reading and writing these fields, and nothing else.
# Such classes are dumb data keepers, and often
# other classes manipulate them into too many details.

# So dataclasses are not that good...
